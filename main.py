"""Entry for the make.fun "Weirdest Job Title: Blind Judge Showdown" bounty.

Writes the job title to entry.txt inside MAKEFUN_OUTPUT_DIR.
Deterministic, no external reads, no network.
"""

import os


# The title is 42 characters — inside the 1-60 gate, written verbatim.
TITLE = "Senior Manager of Meetings About Meetings"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
