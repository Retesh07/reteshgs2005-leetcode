class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        ans = []

        for n, count in freq.items():
            if count == 1:
                ans.append(n)

        return ans