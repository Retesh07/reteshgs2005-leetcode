class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m=min(nums)
        l=max(nums)
        return (l-m)*k
        