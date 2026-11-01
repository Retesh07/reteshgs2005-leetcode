class Solution:
    def minMoves(self, nums: list[int]) -> int:
        total=sum(nums)
        n=len(nums)
        targetsum=min(nums)*n

        return (total-targetsum)
        