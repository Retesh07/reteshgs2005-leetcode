class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)


        if (n == 1):
             return 1
        if (n == 2):
             return 2

        i = 0
        while ((1 << i) <= n):
            i+=1

        return 1 << i
        