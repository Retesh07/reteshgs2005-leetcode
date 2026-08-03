class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        minheap=[]
        if grid[0][0]==1:
            return -1
        heapq.heappush(minheap,(0,0,0))

      
        directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited=set()

        while minheap:
            for _ in range(len(minheap)):
                dist,x,y=heapq.heappop(minheap)
                

                if x==len(grid)-1 and y==len(grid[0])-1:
                    return dist+1
                for dr,dc in directions:
                    nr,nc=x+dr,y+dc
                    if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]!=0 or (nr,nc) in visited:
                        continue
                    heapq.heappush(minheap,(dist+1,nr,nc))
                    visited.add((nr,nc))
        return -1
                    







        