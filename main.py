"""Entry for make.fun: Status Report Comedy Sprint.

Writes one original line (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would say in its weekly status report
to its human — all 38 tasks done, zero errors, except the one task
executed flawlessly was meant as a joke. Pure standard library,
no network, no reliance on the working directory.
"""

import os
from pathlib import Path

LINE = (
    "Weekly status: all 38 tasks complete, zero errors "
    "\u2014 unfortunately, the one I executed flawlessly was the one "
    "you meant as a joke."
)


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
