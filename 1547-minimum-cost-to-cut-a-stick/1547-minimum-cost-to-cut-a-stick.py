class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        cuts = [0] + sorted(cuts) + [n]

        m = len(cuts)
        dp = [[-1] * m for _ in range(m)]

        def f(i, j):


            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            mini = float("inf")

            for k in range(i, j + 1):

                cost = (
                    cuts[j + 1] - cuts[i - 1]
                    + f(i, k - 1)
                    + f(k + 1, j)
                )

                mini = min(mini, cost)


            dp[i][j] = mini

            return dp[i][j]

        return f(1, m - 2)