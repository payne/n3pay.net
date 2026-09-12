---
title: "LXMF references"
description: ""
date: "2026-09-11"
slug: "/posts/lxmf-references-reticulum"
tags:
  - "decentralized"
  - "RF"
  - "ethernet"
draft: false
---

# LXMF References

Reading list gathered while building `lxmf_qr.py` / `qr_lxmf.py`, with a focus on
how keys are managed in Reticulum/LXMF. All links below were confirmed from the
official project metadata bundled with the installed `rns` and `lxmf` pip packages
(`venv/lib/python3.11/site-packages/{rns,lxmf}-*.dist-info/METADATA`).

## Official sources

- **Reticulum manual** — https://markqvist.github.io/Reticulum/manual/ (mirrored at
  https://reticulum.network/manual/). The canonical documentation for the whole
  stack, including identities, cryptography, and interfaces.
  - [Getting Started Fast](https://markqvist.github.io/Reticulum/manual/gettingstartedfast.html)
  - [Using Reticulum](https://markqvist.github.io/Reticulum/manual/using.html) —
    includes the "Included Utility Programs" section covering `rnid`, the identity
    management/encryption CLI tool.
  - [Supported Interfaces](https://markqvist.github.io/Reticulum/manual/interfaces.html)
- **Reticulum source (RNS)** — https://github.com/markqvist/Reticulum — see
  `RNS/Identity.py` for the actual key-handling code.
- **LXMF source** — https://github.com/markqvist/lxmf — see `LXMF/LXMessage.py`
  and `LXMF/LXMRouter.py`.
- **reticulum.network** — https://reticulum.network/ — project home page.
- **FAQ** — https://github.com/markqvist/Reticulum/wiki/Frequently-Asked-Questions

### Client implementations built on LXMF

- Sideband — https://unsigned.io/sideband
- Nomad Network — https://unsigned.io/nomadnet
- MeshChat — https://github.com/liamcottle/reticulum-meshchat

## How keys are managed

This is the short version distilled from `RNS/Identity.py` and `LXMF/LXMRouter.py`
in the installed packages — read those files directly for the authoritative
details.

### The Identity keyset

- A Reticulum `Identity` is a **512-bit Curve25519 keyset**, made of two separate
  256-bit keys (`RNS/Identity.py`, `KEYSIZE`/`CURVE` constants):
  - an **Ed25519** key, used for signing (proves who sent a message)
  - an **X25519** key, used for ECDH key exchange (used to derive per-message
    encryption keys)
- Your Reticulum/LXMF *address* (the destination hash you give out, e.g. an LXMF
  address) is a truncated hash derived from the identity's **public** key. It's
  not a secret and is safe to share; it's how others address messages to you.
- The private key is the only thing that can decrypt messages addressed to that
  identity or produce valid signatures from it. There is no password/passphrase
  wrapping it by default — whoever holds the key file *is* that identity.

### Saving and loading identities

- `Identity.to_file(path)` / `Identity.from_file(path)` are the built-in
  save/load calls (used by both `lxmf_qr.py` and `qr_lxmf.py` via
  `.lxmf_identities/`). The library's own docstring is blunt about the risk:

  > Saves the identity to a file. This will write the private key to disk, and
  > anyone with access to this file will be able to decrypt all communication
  > for the identity. Be very careful with this method.
  > — `RNS/Identity.py`, `to_file()`

  Practical takeaways:
  - Treat an identity file exactly like an SSH private key: don't commit it,
    don't email it, restrict its file permissions. This is why
    `.lxmf_identities/` was added to `.gitignore` in this repo.
  - `pub_to_file(path)` exists separately for saving just the **public** key,
    e.g. to hand your address to someone else without exposing anything secret.
  - `Identity.from_bytes(prv_bytes)` / `load_private_key()` exist for
    lower-level cases, but the docstring explicitly warns never to feed them
    random data to "generate" a key — always use `Identity()` (with
    `create_keys=True`, the default) to actually generate new keys.

### Forward secrecy via ratchets

- A long-term Identity key by itself gives no forward secrecy — if it's ever
  compromised, all past traffic encrypted to it could theoretically be
  decrypted. Reticulum addresses this with **ratchets**: short-lived X25519 keys
  that rotate automatically and are used instead of the long-term key for actual
  message encryption when available (`RNS/Identity.py`, `RATCHETSIZE`,
  `RATCHET_EXPIRY` — defaults to rotating and expiring ratchets after 30 days).
- Real LXMF delivery destinations turn this on via
  `Destination.enable_ratchets(path)`, called from
  `LXMRouter.register_delivery_identity()` in `LXMF/LXMRouter.py` — ratchet keys
  are persisted separately from the identity file, under the router's
  `storagepath/ratchets/` directory.
- **Note on our demo scripts**: `lxmf_qr.py`/`qr_lxmf.py` build a bare
  `RNS.Destination` directly (no `LXMRouter`, no ratchets enabled), so the paper
  message they produce is encrypted with the static identity key only, not a
  ratchet. That's an accurate reflection of how LXMF paper messages actually work
  (they're meant to be decryptable offline, so they can't depend on ratchet state
  that only exists in a live router), but it's worth knowing that a normal,
  online LXMF conversation gets an extra layer of forward secrecy that a
  paper/QR message doesn't.

### Key management tools

- `rnid` — the command-line identity management and encryption utility that
  ships with `rns`. Run `rnid --help` (after `pip install rns`) to see its
  options for generating, inspecting, and using identities from the shell. Covered in
  the "Included Utility Programs" section of the manual link above.

## Suggested reading order

1. Reticulum manual — "Getting Started Fast" (for the big picture).
2. `RNS/Identity.py` in this venv (`venv/lib/python3.11/site-packages/RNS/Identity.py`) —
   read `to_file`, `from_file`, `enable_ratchets`-related code, and the class
   docstring at the top.
3. `LXMF/LXMRouter.py`, `register_delivery_identity()` — how a real LXMF app
   (not just our paper-message demo) sets up its identity and ratchets.
4. The Reticulum manual's cryptographic primitives section (bundled in the `rns`
   package's own README/METADATA) for the exact algorithms in use.
