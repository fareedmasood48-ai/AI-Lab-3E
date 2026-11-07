from lab3_bfs_dfs import GRAPH
FOUND,CUTOFF,FAILURE="FOUND","CUTOFF","FAILURE"
def dls(start,goal,limit,graph=GRAPH):
    def visit(node,path,depth):
        if node==goal: return FOUND,path
        if depth==limit:
            return (CUTOFF if graph.get(node,[]) else FAILURE),None
        cutoff_seen=False
        for nxt in graph.get(node,[]):
            if nxt in path: continue
            status,result=visit(nxt,path+[nxt],depth+1)
            if status==FOUND: return FOUND,result
            if status==CUTOFF: cutoff_seen=True
        return (CUTOFF if cutoff_seen else FAILURE),None
    return visit(start,[start],0)
def iddfs(start,goal,max_depth,graph=GRAPH):
    attempts=[]
    for limit in range(max_depth+1):
        status,path=dls(start,goal,limit,graph); attempts.append((limit,status,path))
        if status==FOUND: return status,path,attempts
        if status==FAILURE: return status,None,attempts
    return CUTOFF,None,attempts
if __name__=="__main__":
    for limit in [1,2,3,4]: print("DLS limit",limit,":",dls("A","G",limit))
    for maximum in [1,2,3,4]: print("IDDFS max",maximum,":",idds if False else iddfs("A","G",maximum))
