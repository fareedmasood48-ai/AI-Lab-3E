from lab3_bfs_dfs import bfs, dfs
from lab3_depth_search import dls, FOUND, FAILURE, CUTOFF
from lab3_ucs import ucs

def run_checks():
    # start equals goal
    assert bfs("A", "A")[0] == ["A"]
    assert dfs("A", "A")[0] == ["A"]
    assert dls("A", "A", 0)[0] == FOUND
    print("PASS: start equals goal")

    # unreachable target
    graph = {"A":["B"], "B":[], "G":[]}
    assert bfs("A", "G", graph)[0] is None
    assert dfs("A", "G", graph)[0] is None
    assert dls("A", "G", 3, graph)[0] == FAILURE
    print("PASS: unreachable goal")

    # cycle must not loop forever
    cycle = {"A":["B"], "B":["A","G"], "G":[]}
    assert bfs("A", "G", cycle)[0] == ["A","B","G"]
    assert dfs("A", "G", cycle)[0] == ["A","B","G"]
    assert dls("A", "G", 2, cycle)[0] == FOUND
    print("PASS: cycle graph")

    path, cost, order = ucs("A","G")
    assert path == ["A","B","E","G"] and cost == 3
    assert sum(__import__("lab3_ucs").WEIGHTS[(u,v)] for u,v in zip(path,path[1:])) == cost
    print("PASS: UCS independent cost sum")
    print("All Lab 3 checks passed.")

if __name__ == "__main__":
    run_checks()
