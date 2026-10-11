class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        i=1
        n=len(nums)
        sums=0
        while i<n+1:
            if n%i==0:
                sums+=nums[i-1]*nums[i-1]
            i+=1
        return sums
            
        