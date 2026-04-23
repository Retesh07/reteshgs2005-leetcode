class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])

        dp=[0]*(n)
        dp[n-1]=1 if obstacleGrid[m-1][n-1]==0 else 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                
                elif j+1<n:


                    dp[j]=dp[j+1]+dp[j]
           
        return dp[0]
        

        