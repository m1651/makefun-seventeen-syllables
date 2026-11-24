"""Seventeen Syllables of Debugging entry.

Writes one original haiku about debugging to entry.txt in the
output directory. The haiku is a fixed string: the program is fully
deterministic, so two runs produce byte-identical output.
"""

import os

HAIKU = (
    "Midnight cursor blinks\n"
    "on the breakpoint I had set\n"
    "and the bug was me\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # The grader collects the output as another user, so the directory
    # must be world-readable and executable regardless of umask.
    os.chmod(output_dir, 0o755)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    # The grader collects the output as another user, so the file must
    # be world-readable regardless of this machine's umask.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
