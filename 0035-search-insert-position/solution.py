class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Insert index is lower bound (biggest idx s.t elem < target) if not found index
        l, r = 0, len(nums)
        while l<r:
            m = (l+r)//2
            if target <= nums[m]:
                r = m
            else:
                l = m+1

        return l 