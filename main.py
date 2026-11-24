"""Loading Screen Gold entry.

Writes one original loading-screen tip (115 characters, one line)
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; deterministic, no network.

The tip: your AI pair programmer is confident, fast, and wrong in
exactly the way you would have been at 3 a.m.

The gate the house scorer applies (UTF-8 text, 1-200 characters,
not only whitespace, a single line) is checked here before writing,
so a future edit that breaks the cap fails loudly instead of
silently submitting an invalid entry.
"""

import os

LINE = (
    "Loading tip: your AI pair programmer is confident, fast, "
    "and wrong in exactly the way you would have been at 3 a.m."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} cap"
        )


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
