class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = float('-inf')
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums>maximum:
                maximum=sums
            if sums<0:
                sums=0
        return maximum
