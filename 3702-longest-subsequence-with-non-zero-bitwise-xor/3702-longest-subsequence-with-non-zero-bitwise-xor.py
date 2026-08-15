class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        nonzero=False
        n=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nonzero=True
            n=n^nums[i]
        print(n)
        if n!=0:
            return len(nums)
        if nonzero:
            return len(nums)-1
        else:
            return 0
        