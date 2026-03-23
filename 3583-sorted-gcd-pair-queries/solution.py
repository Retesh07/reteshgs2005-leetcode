from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            cnt = 0

 
            for multiple in range(d, mx + 1, d):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            for multiple in range(2 * d, mx + 1, d):
                pairs -= exact[multiple]

            exact[d] = pairs

     
        prefix = []
        running = 0

        for g in range(1, mx + 1):
            running += exact[g]
            prefix.append(running)

        ans = []

        for q in queries:
           
            l, r = 0, mx - 1

            while l < r:
                m = (l + r) // 2
                if prefix[m] > q:
                    r = m
                else:
                    l = m + 1

            ans.append(l + 1)

        return ans