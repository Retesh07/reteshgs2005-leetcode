class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        maxarea=0
        count =0
        def dfs(r,c):
            nonlocal count
            
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0 or visited[r][c]:
                return
             
            visited[r][c]=True
            count+=1
            
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
            return count
        

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    c=dfs(i,j)
                    if c>maxarea:
                        maxarea=c
                    count=0
        return maxarea


        