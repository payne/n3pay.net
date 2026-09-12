# Claude Session: LXMF QR Code Encode/Decode

This documents the Claude Code session that produced `lxmf_qr.py` and `qr_lxmf.py`
in this directory.

## Goal

Demonstrate the LXMF "paper message" feature mentioned in `reticulum.md`: LXMF can
represent a fully signed, encrypted message as a QR code, meant to be printed or
scanned rather than transmitted over the network.

Two scripts were built:

1. `lxmf_qr.py` — reads a text file, packs its contents into an LXMF message, and
   saves a QR code of it as a PNG.
2. `qr_lxmf.py` — reads that PNG back, decodes and decrypts the QR code, and writes
   the recovered text to a file.

## Dependencies installed into `venv`

The venv already had `rns` (Reticulum) installed. Added:

```
venv/bin/pip install lxmf qrcode[pil] pillow
venv/bin/pip install opencv-python-headless
```

- `lxmf` — the LXMF protocol library (`LXMessage`, `LXMRouter`, etc.)
- `qrcode[pil]` / `pillow` — used internally by `LXMessage.as_qr()` to render the QR PNG
- `opencv-python-headless` — used by `qr_lxmf.py` (`cv2.QRCodeDetector`) to read a QR
  code back out of a PNG image, without needing a system `zbar` library

## `lxmf_qr.py` — text file → QR PNG

```
venv/bin/python lxmf_qr.py <input_text_file> [output_png_file]
```

Defaults the output path to the input filename with a `.png` extension.

Key design points:

- Builds an `LXMF.LXMessage` with `desired_method=LXMF.LXMessage.PAPER`, which is
  LXMF's built-in representation for a message meant to be encoded as a `lxm://...`
  URI and turned into a QR code, rather than delivered over the network.
- An LXMF message always needs a source and destination `RNS.Identity`/
  `RNS.Destination`, even for a paper message, since the message is still signed by
  the source and encrypted to the destination's public key.
- **Identities are persisted**, not generated fresh each run. They're stored in
  `.lxmf_identities/source_identity` and `.lxmf_identities/destination_identity`
  next to the scripts (created on first run via `RNS.Identity.to_file()`, loaded on
  later runs via `RNS.Identity.from_file()`).
  - This matters because the message content is encrypted to the destination
    identity's public key. If that identity were thrown away after the script
    exited (as an earlier draft did), the resulting QR code would be permanently
    undecryptable — there'd be no private key left anywhere that could open it.
- The QR image itself comes straight from LXMF's own `message.as_qr()` method,
  which internally calls `qrcode.make(...)` and returns a Pillow image.
- LXMF paper messages have a hard capacity limit (`LXMessage.PAPER_MDU`, roughly
  2.2KB of content after protocol overhead, since it all has to fit inside a single
  QR code). If the input file is too large, `as_qr()` raises `TypeError`, which the
  script catches and reports instead of crashing.

## `qr_lxmf.py` — QR PNG → text file

```
venv/bin/python qr_lxmf.py <input_png_file> [output_text_file]
```

Defaults the output path to the input filename with a `.txt` extension.

Key design points:

- Uses `cv2.QRCodeDetector().detectAndDecode(image)` to read the raw `lxm://...`
  URI string out of the PNG.
- Reimplements the inverse of `LXMessage.as_uri()`: strips the `lxm://` scheme,
  restores the base64 padding that was stripped when the URI was built, and
  base64-decodes it back into `paper_packed` bytes (`destination_hash +
  encrypted_data`).
- Loads `.lxmf_identities/destination_identity` (written by `lxmf_qr.py`) and
  builds an `RNS.Destination` from it in the `IN` direction, which is required to
  call `.decrypt()` (a destination built with a public-only identity can only
  `.encrypt()`, not `.decrypt()`).
- Verifies the loaded identity's destination hash actually matches the
  `destination_hash` embedded in the QR data before attempting decryption, and
  fails with a clear message if it doesn't (e.g. wrong identity file, or a QR code
  from a different source).
- Calls `RNS.Destination.decrypt()` to recover the original signed, packed LXMF
  payload, prepends the destination hash back on, and passes the result to
  `LXMF.LXMessage.unpack_from_bytes()` — the exact same code path LXMF's own router
  uses internally when delivering a real message — to get back an `LXMessage` with
  `.content_as_string()` holding the original text.

This mirrors the internals of `LXMRouter.lxmf_propagation()` /
`LXMRouter.lxmf_delivery()` in the installed `lxmf` package (see
`venv/lib/python3.11/site-packages/LXMF/LXMRouter.py`), which was read during this
session to confirm the correct decrypt-then-unpack sequence.

## Verified round trip

Tested end-to-end during the session:

```
$ venv/bin/python lxmf_qr.py message.txt
Wrote QR code PNG to message.png
Destination address: <d13f1678411a8e8bd7f06a5e18d297dc>

$ venv/bin/python qr_lxmf.py message.png decoded.txt
Wrote decoded message content to decoded.txt

$ diff message.txt decoded.txt
(no differences — content matched byte-for-byte)
```

The user separately tried the encoder themselves with `demo.txt` → `demo.png`, and
added a `.gitignore` entry for `venv`.

## Files in this directory after the session

- `lxmf_qr.py` — encoder (text file → QR PNG)
- `qr_lxmf.py` — decoder (QR PNG → text file)
- `.lxmf_identities/` — persisted source/destination identities (created on first
  run of `lxmf_qr.py`; not committed, since it's local key material — add to
  `.gitignore` if keeping this directory around)
- `client.py` / `server.py` — pre-existing "hello world" RNS packet demo (not part
  of this session's work, but the context this session built on)
- `reticulum.md` — the blog post draft that mentions LXMF's QR code feature
