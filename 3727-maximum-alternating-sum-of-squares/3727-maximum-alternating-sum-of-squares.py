
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sums = 0

        for i, val in enumerate(nums):
            nums[i] = val * val

        nums.sort(reverse=True)
        n = len(nums)

        for j in range(len(nums)):
            if j < (n + 1) // 2:
                sums += nums[j]
            else:
                sums -= nums[j]

        return sums
