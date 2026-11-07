import heapq
from lab3_bfs_dfs import GRAPH
# Nonnegative edge costs; C -> G is the explicitly added corridor.
WEIGHTS={("A","B"):1,("A","C"):2,("B","D"):2,("B","E"):1,("C","F"):1,("C","G"):10,("E","G"):1}
WEIGHTED_GRAPH={"A":["B","C"],"B":["D","E"],"C":["F","G"],"D":[],"E":["G"],"F":[],"G":[]}
def ucs(start,goal,graph=WEIGHTED_GRAPH,weights=WEIGHTS):
    frontier=[(0,0,start,[start])]; serial=1; best={start:0}; processed=[]
    while frontier:
        cost,_,node,path=heapq.heappop(frontier)
        if cost!=best.get(node): continue
        processed.append(node)
        if node==goal: return path,cost,processed
        for nxt in graph.get(node,[]):
            new=cost+weights[(node,nxt)]
            if new<best.get(nxt,float("inf")):
                best[nxt]=new; heapq.heappush(frontier,(new,serial,nxt,path+[nxt])); serial+=1
    return None,float("inf"),processed
def bfs_weighted_topology(start,goal):
    from collections import deque
    q=deque([(start,[start])]); seen={start}; processed=[]
    while q:
        node,path=q.popleft(); processed.append(node)
        if node==goal: return path,processed
        for nxt in WEIGHTED_GRAPH[node]:
            if nxt not in seen: seen.add(nxt); q.append((nxt,path+[nxt]))
    return None,processed
if __name__=="__main__":
    path,cost,order=ucs("A","G")
    print("UCS path:",path,"cost:",cost,"processing order:",order)
    bpath,border=bfs_weighted_topology("A","G")
    bcost=sum(WEIGHTS[(u,v)] for u,v in zip(bpath,bpath[1:]))
    print("BFS path:",bpath,"hops:",len(bpath)-1,"cost:",bcost,"processing order:",border)
    print("Independent UCS cost check:",sum(WEIGHTS[(u,v)] for u,v in zip(path,path[1:])))
