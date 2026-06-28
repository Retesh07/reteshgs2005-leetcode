class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=set(nums)
        for i in range(1,len(nums)+2):
            if i not in k:
                return i
        return 1
        