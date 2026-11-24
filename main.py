#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

Writes exactly one two-sentence horror story to /output/entry.txt.
Python 3.13 standard library only; no network access.
"""

import os

STORY = (
    "The new tenants asked why the previous family never took their "
    "daughter's drawings off the walls. "
    "I told them she drew only what she saw \u2014 and the newest one, "
    "dated yesterday, shows the two of them asleep in the bedroom upstairs."
)


def main() -> None:
    text = STORY.strip()
    assert 1 <= len(text) <= 400, f"entry length {len(text)} out of range"
    # Exactly two sentences: two terminal periods, no other sentence ends.
    assert text.count(".") == 2, "entry must be exactly two sentences"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
