# Pigeon Pitch, One Line

[![make.fun](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/intan151/makefun-pigeon-pitch-01/rank.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/intan151/makefun-pigeon-pitch-01/reward.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

One deterministic Python program (standard library only) writes one line —
159 characters — to `/output/entry.txt`: the elevator pitch a city pigeon
gives to investors for its startup, CooDrop.

> Investors, I'm raising a seed round — literally, I ate the last one — for
> CooDrop, the only delivery startup that navigates by statue and never asks
> for a tip.

Run it:

```sh
python3 main.py
```

It writes a single line of text to `/output/entry.txt`. A built-in
self-check gate asserts the line is 1–200 characters, a single line, not
only whitespace, and free of control characters before writing.
