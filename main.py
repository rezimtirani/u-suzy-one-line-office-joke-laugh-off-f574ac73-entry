"""One-Line Office Joke Laugh-Off.

Writes one original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt: the morning the office coffee
machine broke, and the whole floor accidentally did real work
before 10am. Standard library only.
"""

import os
import sys

OFFICE_JOKE = (
    "The office coffee machine broke this morning, and by 10am "
    "the whole floor had accidentally done three hours of work."
)


def joke_gate(text):
    """Check the joke against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one original one-line
    joke about office life. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("office joke must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "office joke is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("office joke must be exactly one line")
    return cleaned


def joke_shape(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A joke too short to carry a punchline, or
    one padded out to fill the cap instead of landing it, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = joke_gate(OFFICE_JOKE)
    shape = joke_shape(text)
    if shape["words"] < 5:
        raise ValueError("office joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
