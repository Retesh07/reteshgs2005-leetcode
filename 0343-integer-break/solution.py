class Solution:
    def integerBreak(self, n: int) -> int:

        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=0

        for target in range(1,n+1):
            for j in range(1,target):
              
                dp[target]=max(dp[target],max(j, dp[j]) * max(target-j, dp[target-j]))
      
        return dp[target]
                



        