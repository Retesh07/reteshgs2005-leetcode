class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<(m*k):
            return -1
        maximum=max(bloomDay)
        l=0
        r=maximum
       
        ans=0
        while l<=r:
            mid=(l+r)//2
            consecutive=0
            boq=0
        

            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    consecutive+=1
                    if consecutive==k:
                        boq+=1
                        consecutive=0
                else:
                    consecutive=0
            if boq>=m:
                ans=mid
                r=mid-1

            else:
                l=mid+1

            
        return ans
                
            


        
        


        
        