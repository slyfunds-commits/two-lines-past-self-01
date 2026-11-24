#!/usr/bin/env python3
"""Two Lines to Your Past Self R1 entry: writes the keeper lines to /output/entry.txt.

Keeper "The Night Shift" (135 chars): two lines joined by a single newline,
no trailing newline. Gate: 1-280 chars UTF-8.
"""
import os

LINE1 = "Say yes to the night shift on 14 March."
LINE2 = "That's the night the factory burns, and you're the only one who knows where the spare keys are."
ENTRY = LINE1 + "\n" + LINE2


def validate(written):
    # The entry is exactly two lines: the warning, then the consequence.
    # One newline joins them; none trails. Gate: 1-280 chars UTF-8.
    assert written == ENTRY, f"entry.txt mismatch: {written!r}"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert written.count("\n") == 1, "entry must be exactly two lines"
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, outside 1-280"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
