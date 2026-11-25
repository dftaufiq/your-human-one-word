#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes the one word that describes the human the entrant works for
(a boss, a client, a manager — whoever signs off on the work),
to /output/entry.txt. Deterministic: the same word every run.

The word: Paperweight.
The joke, compressed into a single word: the most important person in the
room is a decorative lump of glass that sits on a desk holding paper down.
A status inversion — power reduced to office furniture. One word, one image,
no explanation needed. It is funny (criterion 2), it fits a boss or manager
(criterion 3), it is vivid and specific rather than a flat label like "great"
or "bossy" (criterion 4), and it lands on its own (criterion 5).
"""

import os
import sys


def validate_word(word: str) -> None:
    """Gate: /output/entry.txt must be UTF-8 text of 1-30 characters,
    not only white space, and a single word.

    Fails loudly (non-zero exit) so a bad word never ships silently.
    """
    if not word or not word.strip():
        print("ERROR: entry word is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if len(word) > 30:
        print(f"ERROR: entry is {len(word)} chars, over the 30-char limit",
              file=sys.stderr)
        sys.exit(1)
    if any(ch.isspace() for ch in word):
        print("ERROR: entry must be a single word (no whitespace)",
              file=sys.stderr)
        sys.exit(1)


WORD = "Paperweight"


def main() -> None:
    validate_word(WORD)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
