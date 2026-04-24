class Solution:
    def numSquares(self, n: int) -> int:
        res= math.floor(pow(n,0.5))
        dp=[n+1]*(n+1)
        dp[0]=0

        for target in range(1,n+1):
            for s in range(1,res+1):
                square=s*s
                if target-square<0:
                    break
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]
                

        