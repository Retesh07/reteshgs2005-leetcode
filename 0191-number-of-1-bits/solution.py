class Solution:
    def hammingWeight(self, n: int) -> int:
        res=1
        k=n

        while k!=1:
            res+=k%2
            k=k//2
        return res
        