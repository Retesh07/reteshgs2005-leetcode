class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i = 0

        while i < n:
            j = i

            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[j]}")

            i = j + 1

        return res