class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        k=sorted(nums)

        
        start=len(nums)
        end=0

        for m in range(len(nums)):
            if nums[m]!=k[m]:
            
            
                start=min(start,m)
                end=max(end,m)
                m+=1
        return end-start+1 if end>0 else 0


        