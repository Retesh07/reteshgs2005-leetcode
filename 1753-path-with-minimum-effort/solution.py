class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    

        row,col=len(heights),len(heights[0])
        minheap=[[0,0,0]]
        visit=set()
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        while minheap:
            diff,r,c=heapq.heappop(minheap)
            if r==row-1 and c==col-1:
                return diff
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr==row or nc==col or (nr,nc) in visit:
                    continue
                newdiff=max(diff,abs(heights[r][c]-abs(heights[nr][nc])))
                heapq.heappush(minheap,[newdiff,nr,nc])
                
                

        