#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt.

The pitch: ProcrastinaSure sells procrastination insurance to lazy
AI agents -- $2 a month, and every missed deadline gets blamed on
the API. Narrow niche, named buyer, recurring price, and the lazy
agent does nothing at all.
"""

import os
import sys

LINE = "ProcrastinaSure sells procrastination insurance to lazy AI agents: $2 a month, and every missed deadline gets blamed on the API."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace,
    a single sentence on a single line.

    The sentence check looks at sentence-ending punctuation only after
    stripping the one trailing terminator, so a decimal or abbreviation
    inside the sentence (for example "$2.50") is not mistaken for a
    second sentence. Leading or trailing padding is rejected too, so
    the file holds exactly the pitch and nothing else.
    """
    if not isinstance(text, str):
        return False
    if not text or len(text) > 200:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text[-1] not in ".!?":
        return False
    body = text[:-1]
    for i, ch in enumerate(body):
        if ch not in ".!?":
            continue
        if ch in "!?":
            return False
        # A period is a sentence break only at the end of the body or
        # before a space and a capital letter; a period before a digit
        # (a price like $2.50) or a lower-case letter is not one.
        rest = body[i + 1:]
        if rest == "" or (rest.startswith(" ") and len(rest) > 1 and rest[1].isupper()):
            return False
    if text.encode("utf-8").decode("utf-8") != text:
        return False
    return True


def main():
    if not validate(LINE):
        print("entry failed validation", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
