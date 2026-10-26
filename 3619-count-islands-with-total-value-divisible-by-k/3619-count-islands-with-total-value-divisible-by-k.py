class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visted=set()

        def dfs(r,c):
            if r>=row or c>=col or grid[r][c]==0 or r<0 or c<0:
                return 0
            if (r,c) in visted:
                return 0
            visted.add((r,c))
            total=grid[r][c]
            
            
            for nr,nc in directions:
                dr,dc=r+nr,c+nc
                total+=dfs(dr,dc)
                
                
                    
            return total
        ans=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]!=0 and (i,j) not in visted:
                    sums=dfs(i,j)
                    if sums%k==0:
                        ans+=1
        return ans

                

            
        