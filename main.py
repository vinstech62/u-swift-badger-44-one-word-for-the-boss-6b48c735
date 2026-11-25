"""One Word for the Boss — make.fun bounty entry.

Chosen word: Nitpicker

Why this word, judged against the jury criteria:
  * Funny — it paints an instant comic image: a boss who pounces on the
    tiniest flaw while the big picture burns. The joke needs no setup.
  * True — almost everyone has worked for a boss who fusses over
    trivial details (a misaligned label, one typo, the wrong font).
  * Fresh — "micromanager" and "bossy" will flood the entries; "nitpicker"
    is the everyday word people actually use about that boss, yet it is
    far less worn as a bounty answer.
  * Universal — it needs no industry context: a nitpicker exists in a
    kitchen, a warehouse, and an office alike, and the word is understood
    the same way in all three.

Rejected candidates:
  * Helicopter — vivid, but borrows the "helicopter parent" cliche and
    needs a second of decoding; Nitpicker lands immediately.
  * Ghoster — funny and fresh, but it is dating slang first; a boss who
    vanishes is real, yet the word reads less like a boss description.
  * Overpromiser — true, but long, flat, and not funny.
  * Hoverer / Untouchable / Omniscient — either too weak, too
    status-flavoured, or too obscure for an everyday boss word.

The program is deterministic: it always writes the same single word.
"""

import os

WORD = "Nitpicker"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check: exactly one word, letters only, 1-30 characters.
    assert WORD, "word must not be empty"
    assert " " not in WORD and "\t" not in WORD and "\n" not in WORD, (
        "word must be a single word without whitespace"
    )
    assert WORD.isalpha(), "word must contain letters only"
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
