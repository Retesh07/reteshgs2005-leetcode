class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[0]*(amount+1)
        dp[0]=1

        for coin in reversed(coins):
            for a in range(1,amount+1):
                if coin>a:
                    continue
                else:
                    dp[a]=max(dp[a],dp[a]+dp[a-coin])
        return dp[amount]



        