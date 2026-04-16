class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r=0,1
        prev=""
        res=1

        while r<len(arr):
            if arr[r-1]>arr[r] and prev!=">":
                res=max(res,r-l+1)
                r+=1
                prev=">"
            elif arr[r-1]<arr[r] and prev!="<":
                res=max(res,r-l+1)
                r+=1
                prev="<"
            else:
               
                l=r-1 if arr[r]!=arr[r-1] else r
                r+=1

    
                
        return res