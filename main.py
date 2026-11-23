#!/usr/bin/env python3
"""Dad Joke Showdown — entry program.

Writes the single dad joke line to /output/entry.txt.
Standard library only; deterministic — byte-identical on every run.

End-to-end check: verified by running — entry.txt is UTF-8, 159 characters,
161 bytes, one line, not whitespace-only.
"""

import os

LINE = "My wife caught me counting the fence posts and asked what I was doing. I said, 'I'm just trying to picket up where I left off — the neighbors think I'm board.'"


MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
