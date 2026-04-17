class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax,globalmin = nums[0],nums[0]
        total=0
        currmax=0
        currmin=0
        for num in nums:
            currmax = max(num,num+currmax)
            currmin=min(num,num+currmin)
            globalmax=max(globalmax,currmax)
            globalmin=min(globalmin,currmin)
            total+=num
        return max(globalmax,total-globalmin) if globalmax > 0 else   globalmax

        
        