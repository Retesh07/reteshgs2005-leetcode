class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
    
        q=deque()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        cnt=0

        for r in range(row):
            if grid[r][0]==1:
                q.append((r,0))
            if grid[r][col-1]==1:
                q.append((r,col-1))
        for c in range(col):
            if grid[0][c]==1:
                q.append((0,c))
            if grid[row-1][c]==1:
                q.append((row-1,c))
            
        while q:
            r,c=q.popleft()
            if grid[r][c]=='#':
                continue
            grid[r][c]='#'
            
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if nr<0 or nc<0 or nr>=row or nc>=col:
                    continue
                if grid[nr][nc]==1:
                    q.append((nr,nc))
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]=0
                    cnt+=1
   
        return cnt
              

        