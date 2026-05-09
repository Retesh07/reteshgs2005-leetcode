class Solution:
    def findErrorNums(self, nums):
        dup = -1
        missing = -1

        
        for i in range(len(nums)):
            k = abs(nums[i]) - 1

            if nums[k] < 0:
                dup = abs(nums[i])
            else:
                nums[k] = -nums[k]

       
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [dup, missing]