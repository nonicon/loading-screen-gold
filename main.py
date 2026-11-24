"""Loading Screen Gold — one loading-screen tip in 200 characters or fewer.

The grader runs this file (python3.13) and the sealed scorer checks
/output/entry.txt: UTF-8 text, 1-200 characters, not only whitespace.

The tip itself is a single line, written fresh for this bounty. It is a
loading-screen tip for stressed developers *and* AI coding agents at once:
the joke lands because the agent is waiting right beside you, equally unsure
whether the code works — only more confident about it.
"""

import os

# The entry: one line, 110 characters, no trailing newline.
TIP = (
    "Tip: your AI pair programmer has no idea if this works either. "
    "It's just more confident about it than you are."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(tip: str) -> None:
    """The gate, enforced here before anything is written."""
    if not isinstance(tip, str):
        raise TypeError("tip must be str")
    if not tip.strip():
        raise ValueError("tip must not be only whitespace")
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    if not 1 <= len(tip) <= 200:
        raise ValueError(f"tip must be 1-200 characters, got {len(tip)}")


def main() -> None:
    validate(TIP)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the exact line: no trailing newline, so the file's length
    # is the tip's length and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    print(TIP)
    print(f"({len(TIP)} characters -> {OUTPUT_PATH})")


if __name__ == "__main__":
    main()
