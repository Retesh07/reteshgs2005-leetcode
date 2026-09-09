class Solution:
    def countCommas(self, n: int) -> int:

        if n<1000:
            return 0
        power=1000
        ans=0
        while power<=n:
            ans+=n-power+1
            power*=1000
        return ans
        