class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjlist=defaultdict(list)
        for u,v,w in roads:
            adjlist[u].append((v,w))
            adjlist[v].append((u,w))


        
        ways=[0]*n
        distance=[float('inf')]*n
        distance[0]=0
        ways[0]=1
        minheap=[(0,0)]
        MOD=pow(10,9)+ 7
        while minheap:
            dist,node=heapq.heappop(minheap)
            if dist>distance[node]:
                continue
            
         

            for nei,wei in adjlist[node]:
                if dist+wei<distance[nei]:
                    distance[nei]=dist+wei
                    ways[nei]=ways[node]
                    heapq.heappush(minheap,(dist+wei,nei))
                elif dist+wei==distance[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
                  

                
        return ways[n-1]%MOD
            
        