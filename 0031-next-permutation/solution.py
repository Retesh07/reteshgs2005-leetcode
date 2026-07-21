class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modify nums in-place.
        """
        n = len(nums)
        i = n - 2
        ind = -1
        while i>=0:
            if nums[i]<nums[i+1]:
                ind = i
                break
            i-=1
        if ind==-1:
            nums.reverse()
            return nums
        
        j=n-1
        while j>ind:
            if nums[j]>nums[ind]:
                nums[j],nums[ind]=nums[ind],nums[j]
                break
            j-=1
        
        nums[ind+1:]=nums[ind+1:][::-1]
        return nums

        
        
        
    
           
