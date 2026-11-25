#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, at most 280 characters)
to the entry file. Pure standard library.
"""

import os

ENTRY = (
    "Every Sunday, Dad sets a spare plate for the dog. "
    "\"He's family,\" he says, "
    "\"and he's the only one who never complains about my cooking.\""
)


def main() -> None:
    path = os.environ.get("ENTRY_PATH", "/output/entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
