class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        subset = []
        nums.sort()
        
        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Include nums[i]
            subset.append(nums[i])
            create_subset(i+1)
            subset.pop()
            
            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            # Exclude nums[i]
            create_subset(i+1)
        
        create_subset(0)
        return res        