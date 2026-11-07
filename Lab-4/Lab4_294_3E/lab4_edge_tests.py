"""Edge-case and result checks for Lab 4 A*."""
from lab4_astar_audit import search, path_cost

def run_tests():
    graph = {"S": [("A", 1)], "A": [], "G": []}
    h = {"S": 1, "A": 0, "G": 0}
    assert search(graph, h, "S", "S")[0] == ["S"]  # start equals goal
    assert search(graph, h, "S", "G")[0] is None  # unreachable goal
    cyclic = {"S": [("A", 2)], "A": [("S", 1), ("G", 3)], "G": []}
    hc = {"S": 0, "A": 0, "G": 0}
    p, c, *_ = search(cyclic, hc, "S", "G")
    assert p == ["S", "A", "G"] and c == 5
    assert path_cost(cyclic, p) == c
    print("All Lab 4 checks passed (start=goal, unreachable, cycle, path-cost verification).")

if __name__ == "__main__":
    run_tests()
