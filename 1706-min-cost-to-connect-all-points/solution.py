class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minheap=[]
        cost=0
        heapq.heappush(minheap,((0,0)))
        visited=set()

        
        visited=set()
        while minheap:
            dist,i = heapq.heappop(minheap)
            if i in visited:
                continue
            visited.add(i)
            cost+=dist
            for j in range(len(points)):
                if j not in visited:

                    d = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    heapq.heappush(minheap,((d,j)))
        return cost
            

            
        