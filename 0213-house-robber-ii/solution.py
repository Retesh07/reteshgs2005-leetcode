class Solution(object):
    def rob(self, nums):
        return max(nums[0],self.f(nums[:-1]),self.f(nums[1:]))

    def f(self,n):
        rob1,rob2=0,0
        for i in n:
            val=max(i+rob1,rob2)
            rob1=rob2
            rob2=val
        return rob2