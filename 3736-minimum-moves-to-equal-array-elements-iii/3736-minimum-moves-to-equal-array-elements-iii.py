class Solution:
    def minMoves(self, nums: List[int]) -> int:


        maxi=max(nums)
        count=0
        for n in nums:
            count+=maxi-n
        return count
        