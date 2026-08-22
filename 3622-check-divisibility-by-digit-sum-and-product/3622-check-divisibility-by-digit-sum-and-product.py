class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums=0
        product=1
        x=n

        while x>0:
            k=(x%10)
          
            sums+=k

            product*=k
        
            x=x//10
     
        y=sums+product
        print(n%y)
        if n%y==0:
            return True
        return False
        

        