from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1
        k = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[k] = nums[left] * nums[left]
                left += 1
            else:
                ans[k] = nums[right] * nums[right]
                right -= 1

            k -= 1

        return ans