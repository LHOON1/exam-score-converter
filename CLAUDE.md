# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Python script that converts raw exam scores (out of 100) to a grade out of 20, using an exponential curve calibrated so that the cutoff score maps exactly to 10/20.

## Running the script

```bash
python3 convert_scores.py [cutoff]
```

- `cutoff` is optional (default: 65) — the minimum passing score out of 100, accepts decimals (e.g. 67.5)
- Input: `score.csv` (columns: `n`, `name`, `score`)
- Output: `grades.csv` (adds `grade` and `pass` columns)

## Formula

The grade is computed as:

```
s = score / 5                        # convert to /20 scale
grade = s * exp((s - 20) / C)
```

The constant `C` is derived analytically from the cutoff so that `grade(cutoff) = 10/20`:

```
C = (cutoff/5 - 20) / ln(10 / (cutoff/5))
```

This means changing the cutoff requires no manual recalculation of `C` — it is always computed automatically.
