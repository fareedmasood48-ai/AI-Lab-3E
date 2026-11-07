"""Lab 1 - Task 2: rule-based scholarship screening with two extra conditions.
All thresholds are SYNTHETIC LAB ASSUMPTIONS, not real policy.
Review = flag for a human reviewer, NOT an award decision.
Run: python lab1_rules.py
"""

MIN_SCORE = 70          # given in the lab
MIN_GPA = 2.5           # new condition 1: min_gpa_met (synthetic)
LETTER_REQUIRED = True  # new condition 2: recommendation_letter_present (synthetic)


def screen(score, documents_complete, gpa, has_letter):
    """Return (decision, reason) using only explicit, named conditions."""
    if not documents_complete:
        return "Hold", "documents_complete failed"
    if score < MIN_SCORE:
        return "Hold", f"score {score} < {MIN_SCORE}"
    if gpa < MIN_GPA:
        return "Hold", f"min_gpa_met failed ({gpa} < {MIN_GPA})"
    if LETTER_REQUIRED and not has_letter:
        return "Hold", "recommendation_letter_present failed"
    return "Review", "all conditions satisfied"


# Exactly four core tests: pass, fail of each new condition, threshold boundary.
tests = [
    # name,               score, docs_ok, gpa, letter, expected
    ("pass_all",            82, True, 3.2, True,  "Review"),
    ("fail_low_gpa",        85, True, 2.1, True,  "Hold"),
    ("fail_no_letter",      88, True, 3.5, False, "Hold"),
    ("boundary_exact",      70, True, 2.5, True,  "Review"),
]

print("case | input | expected | actual | reason | match")
all_ok = True
for name, score, docs, gpa, letter, expected in tests:
    actual, reason = screen(score, docs, gpa, letter)
    ok = actual == expected
    all_ok &= ok
    inp = f"score={score},docs={docs},gpa={gpa},letter={letter}"
    print(name, inp, expected, actual, reason, "PASS" if ok else "FAIL", sep=" | ")

print("\nAll tests passed:", all_ok)
