class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        memo=[[0]*c for _ in range(r)]

        def dfs(i,j):
            if i==r-1 and j==c-1:
                return grid[i][j]
            if i==r or j==c:
                return float('inf')
            if memo[i][j]:
                return memo[i][j]
            memo[i][j]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
            return memo[i][j]
        return dfs(0,0)

        