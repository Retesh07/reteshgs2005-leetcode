class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(dict)

        for i,e in enumerate(equations):
            a,b=e
            adj[a][b]=values[i]
            adj[b][a]=1/(values[i])
        for k in adj:
            for i in adj[k]:
                for j in adj[k]:
                    if j not in adj[i]:
                        adj[i][j]=adj[i][k]*adj[k][j]
        res=[]
        for q1,q2 in queries:
            if q1 in adj and q2 in adj[q1]:
                res.append(adj[q1][q2])
            else:
                res.append(-1.0)
        return res



        
        