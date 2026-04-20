class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        left, right = 0, 1
        count = 0
        ans = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[right] == nums[right] - nums[left]:
                count += 1
                ans += count
            else:
                count = 0

            left += 1
            right += 1

        return ans