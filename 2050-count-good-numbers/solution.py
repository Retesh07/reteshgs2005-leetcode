class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        def pow(x,w):
            res=1
            while w>0:
                if w%2:
                    res=(res*x)%mod
                x=(x*x)%mod
                w=w//2
            return res


        even=ceil(n/2)
        odd=n//2
        return (pow(5,even)*pow(4,odd))%mod
        