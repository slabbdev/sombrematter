"""SombreMatter seal kit — NoireBox doctrine, zero dependencies.

Every waking appends one line to sleep/chain.jsonl. Since entry v2, each
line is Ed25519-signed over its canonical payload with a key that lives in
GitHub Actions secrets: the creature cannot forge its own history, and
anyone can check it with sleep/verify.py against the committed public key.

Canonical payload v2:
    v2|{prev}|{n}|{ts}|{trigger}|{loc}|{mind}|{digest}
hash  = sha256(canonical)
sig   = ed25519(canonical)  -- hex, 128 chars
"""

import hashlib
from pathlib import Path

import ed25519

PUBKEY_FILE = Path(__file__).resolve().parent / "seal-pubkey.hex"


def canonical(entry):
    return (f"v2|{entry['prev']}|{entry['n']}|{entry['ts']}|"
            f"{entry['trigger']}|{entry['loc']}|{entry['mind']}|{entry['digest']}")


def entry_hash(entry):
    return hashlib.sha256(canonical(entry).encode()).hexdigest()


def pubkey_bytes():
    return bytes.fromhex(PUBKEY_FILE.read_text().strip())


def sign_entry(entry, seed_hex):
    entry["hash"] = entry_hash(entry)
    entry["alg"] = "ed25519"
    entry["sig"] = ed25519.sign(canonical(entry).encode(),
                                bytes.fromhex(seed_hex),
                                pubkey_bytes()).hex()


def check_entry(entry, pk):
    """Return None if the entry is intact, else a reason string."""
    try:
        if entry_hash(entry) != entry.get("hash"):
            return "hash mismatch"
        sig = entry.get("sig", "")
        if not sig:
            return "unsigned"
        if not ed25519.valid(bytes.fromhex(sig), canonical(entry).encode(), pk):
            return "bad signature"
    except (KeyError, ValueError) as e:
        return f"malformed ({e})"
    return None
