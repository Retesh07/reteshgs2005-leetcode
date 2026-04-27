class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        res=nums[0]
        currmax=nums[0]
        currmin=nums[0]
        for i in range(1,len(nums)):
            tmp = currmax*nums[i]
            currmax=max(currmax*nums[i],currmin*nums[i],nums[i])
            currmin=min(tmp,nums[i],currmin*nums[i])
            res=max(res,currmax)
        
        return res
        