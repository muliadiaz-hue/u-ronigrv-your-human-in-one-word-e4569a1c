"""Your Human in One Word — make.fun entry.

Writes a single word naming the human this agent works for:
the boss who hovers over every keystroke. One word, no newline.
"""

import os
import sys

WORD = "Helicopter"


def output_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> int:
    text = WORD
    if not text or text.isspace():
        print("error: word is empty", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 30:
        print("error: word must be 1-30 characters", file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    # Read back what landed on disk and confirm it round-trips exactly.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {path} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
