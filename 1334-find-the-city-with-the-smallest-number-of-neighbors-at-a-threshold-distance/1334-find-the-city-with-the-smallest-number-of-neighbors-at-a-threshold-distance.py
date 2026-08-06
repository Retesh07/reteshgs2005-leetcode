class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjlist=defaultdict(list)
        for u,v,w in edges:
            adjlist[u].append((v,w))
            adjlist[v].append((u,w))
        smallest_city=float("-inf")
        res=[0]*n
        
        for cities in range(n):
            dist=[float("inf")]*(n)
            q=[]
            q.append((0,cities))
            dist[cities]=0
            while len(q):
                weigh,c=heapq.heappop(q)
                if weigh>dist[c]:
                    continue
                
                for neigh, w in adjlist[c]:
                    if dist[neigh]>w+weigh and w+weigh<=distanceThreshold:
                        dist[neigh]=w+weigh
                        heapq.heappush(q,(w+weigh,neigh))
            cnt=0
            for i in range(len(dist)):
                if dist[i]!=float("inf"):
                    cnt+=1
            res[cities]=cnt
        ck=min(res)
        result=-1
        for i in range(len(res)):
            if res[i]==ck:
                result=i
        return result

            
            




            
        