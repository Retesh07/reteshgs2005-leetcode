class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c=defaultdict(int)
        maxlen=float("-inf")
        l=0

        for r in range(len(nums)):
            c[nums[r]]+=1
            if c[nums[r]]<=k:
                maxlen=max(r-l+1,maxlen)
            else:
                while c[nums[r]]>k:
                
                    c[nums[l]]-=1
                    l+=1
        return maxlen
        