import base64
import os
import sys

import cv2
import RNS
import LXMF
from LXMF.LXMessage import LXMessage

IDENTITY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".lxmf_identities")

def load_identity(path):
    if not os.path.isfile(path):
        print(f"No identity found at {path}. Was this QR code generated with lxmf_qr.py?")
        sys.exit(1)
    return RNS.Identity.from_file(path)

def decode_qr(input_path):
    image = cv2.imread(input_path)
    if image is None:
        print(f"Could not read image file: {input_path}")
        sys.exit(1)

    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(image)
    if not data:
        print("No QR code could be found in the image.")
        sys.exit(1)

    return data

def unpack_lxm_uri(uri, destination_identity):
    if not uri.lower().startswith(LXMessage.URI_SCHEMA + "://"):
        print(f"Data found in QR code is not an LXMF URI: {uri}")
        sys.exit(1)

    encoded = uri[len(LXMessage.URI_SCHEMA + "://"):]
    # Restore the base64 padding that was stripped off when the URI was made.
    encoded += "=" * (-len(encoded) % 4)
    paper_packed = base64.urlsafe_b64decode(encoded)

    destination_hash = paper_packed[:LXMessage.DESTINATION_LENGTH]
    encrypted_data = paper_packed[LXMessage.DESTINATION_LENGTH:]

    destination = RNS.Destination(
        destination_identity,
        RNS.Destination.IN,
        RNS.Destination.SINGLE,
        "lxmf",
        "delivery"
    )

    if destination.hash != destination_hash:
        print("The provided identity does not match the destination this message was addressed to.")
        sys.exit(1)

    decrypted_data = destination.decrypt(encrypted_data)
    if decrypted_data is None:
        print("Decryption failed.")
        sys.exit(1)

    lxmf_bytes = destination_hash + decrypted_data
    return LXMessage.unpack_from_bytes(lxmf_bytes)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input_png_file> [output_text_file]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.rsplit(".", 1)[0] + ".txt"

    # Initialize Reticulum
    RNS.Reticulum()

    destination_identity = load_identity(os.path.join(IDENTITY_DIR, "destination_identity"))

    uri = decode_qr(input_path)
    message = unpack_lxm_uri(uri, destination_identity)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(message.content_as_string())

    print(f"Wrote decoded message content to {output_path}")

if __name__ == "__main__":
    main()
