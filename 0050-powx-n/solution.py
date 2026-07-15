class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        nn=n
        ans=1.0
        if nn<0:
            nn = -n
        while(nn>0):
            if nn%2==1:
                ans=ans*x
                nn-=1
            else:
                x=x*x
                nn=nn//2
        if n<0:
            ans=1/ans
        return ans