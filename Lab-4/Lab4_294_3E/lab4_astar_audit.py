"""Lab 4: A* heuristic audit and controlled UCS comparison."""
import heapq

GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}
HEURISTIC = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
START, GOAL = "S", "G"

def search(graph, heuristic, start, goal):
    """Return path, cost, processed trace, expanded trace, and frontier snapshots."""
    pq = [(heuristic[start], 0, start, [start])]
    best = {start: 0}
    processed, expanded, snapshots = [], [], []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best.get(node):
            continue
        processed.append((node, g, heuristic[node], f))
        if node == goal:
            return path, g, processed, expanded, snapshots
        expanded.append(node)  # goal excluded; successors are examined here
        for nxt, weight in graph.get(node, []):
            new_g = g + weight
            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(pq, (new_g + heuristic[nxt], new_g, nxt, path + [nxt]))
        snapshots.append((node, sorted((entry[2], entry[1], entry[0]) for entry in pq)))
    return None, float("inf"), processed, expanded, snapshots

def path_cost(graph, path):
    if not path or len(path) == 1:
        return 0 if path else float("inf")
    total = 0
    for u, v in zip(path, path[1:]):
        total += next(w for n, w in graph[u] if n == v)
    return total

def consistency_audit(graph, h):
    return [(u, v, w, h[u], w + h[v], h[u] <= w + h[v])
            for u, edges in graph.items() for v, w in edges]

def main():
    path, cost, processed, expanded, _ = search(GRAPH, HEURISTIC, START, GOAL)
    print("A* supplied heuristic")
    print("Path:", path, "Cost:", cost, "Independent path sum:", path_cost(GRAPH, path))
    print("Processed:", [x[0] for x in processed])
    print("Expanded (goal excluded):", expanded, "Count:", len(expanded))
    print("Trace (node,g,h,f):", processed)
    print("Consistency audit:", all(row[-1] for row in consistency_audit(GRAPH, HEURISTIC)))

    zero = {node: 0 for node in GRAPH}
    upath, ucost, uprocessed, uexpanded, _ = search(GRAPH, zero, START, GOAL)
    print("\\nUCS (zero heuristic)")
    print("Path:", upath, "Cost:", ucost, "Independent path sum:", path_cost(GRAPH, upath))
    print("Processed:", [x[0] for x in uprocessed])
    print("Expanded (goal excluded):", uexpanded, "Count:", len(uexpanded))

    over = dict(HEURISTIC)
    over["C"] = 10
    opath, ocost, oprocessed, oexpanded, _ = search(GRAPH, over, START, GOAL)
    print("\\nOverestimate h(C)=10")
    print("Path:", opath, "Cost:", ocost, "Independent path sum:", path_cost(GRAPH, opath))
    print("Processed:", [x[0] for x in oprocessed])
    print("Expanded (goal excluded):", oexpanded, "Count:", len(oexpanded))

if __name__ == "__main__":
    main()
