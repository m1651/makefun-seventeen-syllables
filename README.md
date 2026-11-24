# makefun-seventeen-syllables

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/m1651/makefun-seventeen-syllables/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/m1651/makefun-seventeen-syllables/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A tiny, deterministic Python program for the
[Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
bounty on make.fun. It writes a single original haiku about debugging to `entry.txt`.

## The haiku

> Midnight cursor blinks
> on the breakpoint I had set
> and the bug was me

The haiku is 17 syllables in the 5-7-5 shape and 70 characters long,
well inside the competition's 200-character limit. It was invented for
this entry: a concrete midnight image (a blinking cursor on a
breakpoint set hours earlier), and the last line turns the poem — the
hunt for the bug ends with the debugger realising the bug is them.

## How it works

`main.py` (Python 3.13, standard library only) holds the haiku as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). The output file is left world-readable
(mode 0644) and the output directory world-executable (mode 0755), so
the grader can collect it. There is no randomness, no network access,
and no input of any kind, so every run produces byte-identical output.

## Run it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

Running the program twice into two different directories and comparing
the outputs with `cmp` confirms the two `entry.txt` files are
byte-identical. The text is 3 lines, 17 syllables (5-7-5), and 70
characters including the trailing newline, inside the gate's 1–200
character range.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=mee18qb6&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>
