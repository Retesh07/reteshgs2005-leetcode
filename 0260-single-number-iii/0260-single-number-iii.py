class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xr=0
        for x in nums:
            xr^=x
        bit=xr&-xr

        a=0
        b=0
        for n in nums:
            if n & bit:
                a^=n
            else:
                b^=n
        return [a,b]
        