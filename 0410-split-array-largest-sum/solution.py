class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)

        while l<=r:
            mid=l+(r-l)//2
            m= self.splits(nums,mid)
            if m>k:
                l=mid+1
            else:
                r=mid-1
        return l

        
    def splits(self,nums,mid):

        split=1
        sums=0
        for num in nums:
            if num+sums<=mid:
                sums+=num
            else:
                split+=1
                sums=num
        return split




        