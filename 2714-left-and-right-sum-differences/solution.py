class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = [0] * n
        
        
        for i in range(1, n):
            diff[i] = diff[i-1] + nums[i-1]
        
        total = sum(nums)
        
        
        for i in range(n):
            right = total - diff[i] - nums[i]
            diff[i] = abs(diff[i] - right)
        
        return diff