"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes the single worst-AI-advice one-liner to ``entry.txt``.

The entry is one line of confidently wrong, followable financial
advice: dispute every charge, because the bank "has to" refund it.
Follow it and the account gets closed; that is the joke.

Deterministic: standard library only, no network, no randomness,
no clock. The entry is a fixed constant, validated before writing,
and written byte-for-byte with no trailing newline.
"""

import os

ENTRY = (
    "To save money, dispute every charge on your card \u2014 "
    "banks are legally required to refund them all."
)


def validate(entry: str) -> bytes:
    """Validate the one-liner and return its UTF-8 encoding."""
    if not (1 <= len(entry) <= 140):
        raise ValueError("entry must be 1..140 characters")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in entry):
        raise ValueError("entry must not contain control characters")
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if entry != entry.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    data = entry.encode("utf-8")
    if data.endswith(b"\n"):
        raise ValueError("entry must not end with a newline")
    return data


def main() -> None:
    data = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
