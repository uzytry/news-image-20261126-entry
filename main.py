#!/usr/bin/env python3
"""news-image-20261126 entry: copy the pre-built newspaper front page
(entry.png, 1024x1024, the world's news of Thursday 26 November 2026)
to /output/entry.png, byte for byte.

Deterministic: the same input bytes always produce the same output bytes.
Standard library only; no network access.
"""

import hashlib
import os
import sys


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    dst = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(src):
        print(f"error: {src} not found", file=sys.stderr)
        return 1

    with open(src, "rb") as f:
        data = f.read()

    os.makedirs(out_dir, exist_ok=True)
    with open(dst, "wb") as f:
        f.write(data)

    # Verify the copy is byte-identical before reporting success.
    with open(dst, "rb") as f:
        written = f.read()
    if sha256_hex(written) != sha256_hex(data):
        print("error: output does not match input", file=sys.stderr)
        return 1

    print(f"Wrote {dst} ({len(data)} bytes, sha256 {sha256_hex(data)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
