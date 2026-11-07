"""Lab 1 - Section 1.5: symbolic rule vs probability threshold.
NOTE: probabilities are invented demonstration inputs. No model is trained,
so this is a BEHAVIOUR comparison, not an accuracy experiment.
Run: python lab1_compare.py
"""


def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"


def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"


cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]

print("case | symbolic | threshold | disagreement")
for name, score, complete, probability in cases:
    a, b = symbolic(score, complete), threshold(probability)
    print(name, a, b, a != b, sep=" | ")

# Section 1.6 isolation test: change boundary score and probability separately
print("\n--- Section 1.6: isolating the boundary case ---")
print("score=69, complete=True        ->", symbolic(69, True))
print("probability=0.69               ->", threshold(0.69))
print("score=70, complete=False       ->", symbolic(70, False))
