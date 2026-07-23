class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        k = (l * (l + 1)) // 2  
        total = sum(nums)
        return k - total
