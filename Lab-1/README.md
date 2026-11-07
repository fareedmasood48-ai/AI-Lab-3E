# Lab 1 – Introduction to AI & Paradigms (CAI601400)

Author: Rasikh Ali (42365)

## Contents
| File | Purpose |
|---|---|
| `lab1_compare.py` | Symbolic rule vs probability threshold (Section 1.5 / 1.6) |
| `lab1_rules.py` | Rule system with two extra conditions + four core tests (Task 2) |
| `compare_output.txt` | Captured output of `lab1_compare.py` |
| `rules_output.txt` | Captured output of `lab1_rules.py` |
| `Lab1_Report.docx` | Full report (timeline, tests, disagreement table, comparison) |

## Setup
Requires Python 3.8+. No external packages.

```bash
python --version
```

## Run
```bash
python lab1_compare.py
python lab1_rules.py
```

## Assumptions
- All thresholds (score >= 70, GPA >= 2.5, letter required) are **synthetic lab assumptions**.
- Probabilities in `lab1_compare.py` are **invented demo inputs**; no model is trained.
- `Review` means "flag for a human reviewer", not an award decision.
- No credentials, private data or virtual environments are included.
