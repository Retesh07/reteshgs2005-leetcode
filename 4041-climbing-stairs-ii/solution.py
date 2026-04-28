class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp=[0]*(n+1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')

            if i + 1 <= n:
                dp[i] = min(
                    dp[i],
                    costs[i] + 1 + dp[i + 1]
                )

            if i + 2 <= n:
                dp[i] = min(
                    dp[i],
                    costs[i + 1] + 4 + dp[i + 2]
                )

            if i + 3 <= n:
                dp[i] = min(
                    dp[i],
                    costs[i + 2] + 9 + dp[i + 3]
                )
        return dp[0]
            