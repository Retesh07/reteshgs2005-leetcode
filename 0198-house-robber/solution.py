class Solution:
    def rob(self, nums):

        memo = {}

        def dfs(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            take = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            memo[i] = max(take, skip)

            return memo[i]

        return dfs(0)