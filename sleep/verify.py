#!/usr/bin/env python3
"""SombreMatter — public seal verifier.

Anyone can check that the creature's life has not been rewritten:

    python3 sleep/verify.py

Verifies, for every entry of sleep/chain.jsonl:
  - numbering (1, 2, 3, ...) and hash-chain linkage (prev -> hash),
  - from the first signed entry onward: sha256 of the canonical payload
    AND its Ed25519 signature against sleep/seal-pubkey.hex.

Entries before the signed era carry no signature (they are anchored only
by git history); that is expected and reported. Exits 1 on any anomaly.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import seal  # noqa: E402

CHAIN = Path(__file__).resolve().parent / "chain.jsonl"


def verify_chain(chain_path=CHAIN):
    pk = seal.pubkey_bytes()
    lines = chain_path.read_text().splitlines()
    prev, signed_era, problems = "", False, []
    legacy = signed = 0
    for i, line in enumerate(lines, 1):
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            problems.append(f"entry {i}: not JSON")
            continue
        n = e.get("n")
        if n != i:
            problems.append(f"entry {i}: numbering broken (n={n})")
        if e.get("prev") != prev:
            problems.append(f"entry {i}: broken link (prev != previous hash)")
        is_signed = bool(e.get("sig"))
        if is_signed:
            signed_era = True
            signed += 1
        elif signed_era:
            problems.append(f"entry {i}: unsigned in the signed era")
        else:
            legacy += 1
        if signed_era or is_signed:
            reason = seal.check_entry(e, pk)
            if reason:
                problems.append(f"entry {i}: {reason}")
        prev = e.get("hash", prev)
    return not problems, problems, {"entries": len(lines), "legacy": legacy,
                                    "signed": signed}


def main():
    if not CHAIN.exists():
        sys.exit("verify: no chain yet — the creature has no history")
    ok, problems, stats = verify_chain()
    if ok:
        print(f"verify: chain intact — {stats['entries']} entries "
              f"({stats['legacy']} legacy, {stats['signed']} signed)")
    else:
        for p in problems:
            print(f"verify: TAMPERED — {p}")
        sys.exit(1)


if __name__ == "__main__":
    main()
