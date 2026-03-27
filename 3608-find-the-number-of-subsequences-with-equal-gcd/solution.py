class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        cache={}
        n=len(nums)
        MOD=10**9+7
        

        def dfs(i, g1, g2):

            state = (i, g1, g2)

            if state in cache:
                return cache[state]

            if i == n:
                cache[state] = 1 if g1 > 0 and g2 > 0 and g1 == g2 else 0
                return cache[state]

            x = nums[i]

            ans = (
                dfs(i + 1, gcd(g1, x), g2)
                + dfs(i + 1, g1, gcd(g2, x))
                + dfs(i + 1, g1, g2)
            ) % MOD

            cache[state] = ans
            return ans
        return dfs(0,0,0)