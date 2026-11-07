from collections import deque
GRAPH = {"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def bfs(start, goal, graph=GRAPH):
    queue=deque([(start,[start])]); seen={start}; processed=[]
    while queue:
        node,path=queue.popleft(); processed.append(node)
        if node==goal: return path,processed
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt); queue.append((nxt,path+[nxt]))
    return None,processed
def dfs(start, goal, graph=GRAPH):
    stack=[(start,[start])]; seen=set(); processed=[]
    while stack:
        node,path=stack.pop()
        if node in seen: continue
        seen.add(node); processed.append(node)
        if node==goal: return path,processed
        for nxt in reversed(graph.get(node,[])):
            if nxt not in seen: stack.append((nxt,path+[nxt]))
    return None,processed
if __name__=="__main__":
    print("BFS path, processed:",bfs("A","G"))
    print("DFS path, processed:",dfs("A","G"))
