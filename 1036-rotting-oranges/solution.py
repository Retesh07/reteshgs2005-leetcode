class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        row,col=len(grid),len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                    grid[r][c]=2
                elif grid[r][c]==1:
                    fresh+=1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        cnt=0
        if fresh==0:
            return 0

        while q and fresh:
            
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if nr<0 or nc<0 or nr>=row or nc>=col or grid[nr][nc]==2 or grid[nr][nc]==0:
                        continue
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            cnt+=1
        
        return cnt if fresh<=0 else -1


        