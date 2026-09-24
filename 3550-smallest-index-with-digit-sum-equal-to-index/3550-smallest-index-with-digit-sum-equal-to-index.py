class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            strs=str(nums[i])

            c=0
            for j in range(len(strs)):
                c+=int(strs[j])
            if c==i:
                return i
        return -1
        
        