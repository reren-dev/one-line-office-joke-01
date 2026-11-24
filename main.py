#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original one-line joke about office life to
/output/entry.txt: 1-200 characters, one line, no trailing newline.
"""

import os

JOKE = "The office plant died, so we called a meeting about it \u2014 the plant is still dead, but now it has action items."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 characters, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
