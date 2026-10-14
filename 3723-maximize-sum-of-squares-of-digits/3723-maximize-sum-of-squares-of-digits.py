class Solution:
    def maxSumOfSquares(self, num: int, target_sum: int) -> str:
        if target_sum > 9 * num:
            return ""
        

        st=""
        k=num
        remaining=target_sum
        
        while k>0:
            for i in range(9,-1,-1):
                if i<=remaining:
                
                    st+=str(i)
                    remaining-=i
                    break
                
            
              
            k-=1
        return st if remaining==0 else ""
        