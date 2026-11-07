"""Edge and equivalence tests for Lab 5."""
from lab5_minimax_audit import minimax, alphabeta

def test():
    # A one-level tree: MAX chooses 7.
    scores = [4, 7]
    m, a = [0], [0]
    mv = minimax(0, 0, True, scores, 1, m)
    av = alphabeta(0, 0, True, scores, 1, float("-inf"), float("inf"), a)
    assert mv == av == 7
    assert m[0] == 2 and a[0] == 2

    # Main supplied 8-leaf tree: same optimal root value.
    scores = [3, 5, 2, 9, 3, 5, 2, 9]
    m, a = [0], [0]
    mv = minimax(0, 0, True, scores, 3, m)
    av = alphabeta(0, 0, True, scores, 3, float("-inf"), float("inf"), a)
    assert mv == av == 5
    assert a[0] <= m[0]
    print("All Lab 5 checks passed (depth-1 edge case, value equivalence, leaf-count bound).")

if __name__ == "__main__":
    test()
