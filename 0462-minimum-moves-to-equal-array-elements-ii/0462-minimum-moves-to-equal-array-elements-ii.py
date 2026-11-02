class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        count=0
        for n in nums:
            count+=abs(n-nums[mid])
        return count

        