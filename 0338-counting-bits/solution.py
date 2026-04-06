class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            result.append(self.binary(i))
        return result



    def binary(self,n):
        res=0
        k=n

        while k:
            res+=k%2
            k=k//2
        return res
        