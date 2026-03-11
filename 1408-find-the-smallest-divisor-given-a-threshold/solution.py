class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        ans=-1

        while l<=r:
            mid=(l+r)//2
            nu=0
            for num in nums:
                nu+=math.ceil(num/mid)
            if nu>threshold:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans


        