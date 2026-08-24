class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        sums=0

        for i in range(len(nums)):
            if i%2==0:
                sums+=nums[i]
            else:
                sums-=nums[i]
        return sums

        