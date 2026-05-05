class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap=[]
        visited=set()
        row,col =len(grid),len(grid[0])
        cost=0
        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        heapq.heappush(minheap,((grid[0][0],0,0)))
        while minheap:
            dist,r,c = heapq.heappop(minheap)
            cost = max(dist,cost)
            if r<0 or c<0 or r==row or c==col or (r,c) in visited:
                continue
            if r==row-1 and c==col-1:
                return cost
            visited.add((r,c))
            for dr,dc in dir:
                nr,nc = r+dr , c+dc

                if nr<0 or nc<0 or nr==row or nc==col or (nr,nc) in visited:
                    continue
                d  = grid[nr][nc]
                
                heapq.heappush(minheap,((d,nr,nc)))
        return 0


            
        

        