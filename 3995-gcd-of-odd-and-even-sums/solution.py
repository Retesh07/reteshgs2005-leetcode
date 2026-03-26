class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=(pow(n,2))
        sumEven=n*(n+1)

        return self.gcd(sumOdd,sumEven)
    def gcd(self,a,b):
        if b>a:
            a,b=b,a
        if b==0:
            return a
        return self.gcd(b,a%b)
        
        
        

        