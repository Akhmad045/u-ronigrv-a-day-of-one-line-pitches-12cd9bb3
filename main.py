"""A Day of One-Line Pitches — make.fun sprint entry.

Assembles the single-sentence pitch from LINES, checks it is one
sentence of 1-240 characters, and writes it to /output/entry.txt.
"""

import os

LINES = [
    "You describe your app idea in plain words, an AI agent on make.fun "
    "builds a working app from it, and you can try it, tweak it, and "
    "share it - no coding needed, just your idea.",
]

MAX_CHARS = 240


def main():
    sentence = "".join(LINES).strip()
    assert sentence, "entry must not be empty"
    assert len(sentence) <= MAX_CHARS, (
        f"entry is {len(sentence)} chars, over the {MAX_CHARS} limit"
    )
    assert sentence.endswith(".") and ". " not in sentence, (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    print(f"entry ({len(sentence)} chars): {sentence}")


if __name__ == "__main__":
    main()
