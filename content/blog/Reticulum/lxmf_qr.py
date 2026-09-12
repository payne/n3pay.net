import os
import sys

import RNS
import LXMF

IDENTITY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".lxmf_identities")

def load_or_create_identity(path):
    if os.path.isfile(path):
        return RNS.Identity.from_file(path)
    identity = RNS.Identity()
    identity.to_file(path)
    return identity

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input_text_file> [output_png_file]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.rsplit(".", 1)[0] + ".png"

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Initialize Reticulum
    RNS.Reticulum()

    # A paper message is never actually sent over the network, but LXMF still
    # needs a source and destination identity so it can sign and encrypt it,
    # just like a normal message. The destination identity's private key is
    # what a decoder needs to decrypt the message later, so both identities
    # are persisted to disk instead of being thrown away after this run.
    os.makedirs(IDENTITY_DIR, exist_ok=True)
    source_identity = load_or_create_identity(os.path.join(IDENTITY_DIR, "source_identity"))
    destination_identity = load_or_create_identity(os.path.join(IDENTITY_DIR, "destination_identity"))

    source = RNS.Destination(
        source_identity,
        RNS.Destination.IN,
        RNS.Destination.SINGLE,
        "lxmf",
        "delivery"
    )

    destination = RNS.Destination(
        destination_identity,
        RNS.Destination.OUT,
        RNS.Destination.SINGLE,
        "lxmf",
        "delivery"
    )

    message = LXMF.LXMessage(
        destination,
        source,
        content,
        desired_method=LXMF.LXMessage.PAPER
    )

    try:
        qr_image = message.as_qr()
    except TypeError as e:
        # Raised by LXMF when the file's content is too large to fit in a
        # single QR code (~2.2KB after LXMF/Reticulum overhead).
        print(f"Could not encode message as a QR code: {e}")
        sys.exit(1)

    qr_image.save(output_path)
    print(f"Wrote QR code PNG to {output_path}")
    print(f"Destination address: {RNS.prettyhexrep(destination.hash)}")

if __name__ == "__main__":
    main()
