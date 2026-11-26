#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun bounty
u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Writes one line (<=200 chars) to /output/entry.txt: the elevator pitch
a city pigeon gives to investors for its startup, CooDrop.
Stdlib only, deterministic, no network, no randomness.
"""
import os

LINE = "Investors, I'm raising a seed round \u2014 literally, I ate the last one \u2014 for CooDrop, the only delivery startup that navigates by statue and never asks for a tip."

def main():
    # Self-check gate (mirrors the RULES.txt gate): 1-200 chars, one line,
    # not only whitespace, no control characters, valid UTF-8.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert all(ord(ch) >= 32 or ch in "\t" for ch in LINE), "no control characters"
    LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
