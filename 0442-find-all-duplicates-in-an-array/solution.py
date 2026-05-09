class Solution:
    def findDuplicates(self, nums):
        ans = []

        for i in range(len(nums)):
            k = abs(nums[i]) - 1

            if nums[k] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[k] = -nums[k]

        return ans