class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

      
        
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                r=mid-1
        if r==-1:
            return k
        beforemissing=arr[r]-(r+1)
        return arr[r]+(k-beforemissing)        