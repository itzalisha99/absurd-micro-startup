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
    a single sentence on a single line."""
    if not isinstance(text, str):
        return False
    if not text or len(text) > 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    text.encode("utf-8")
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
