class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []

        for i in range(len(nums)):
            indx = abs(nums[i]) - 1
            if nums[indx] > 0:
                nums[indx] = -nums[indx]

        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j + 1)

        return res