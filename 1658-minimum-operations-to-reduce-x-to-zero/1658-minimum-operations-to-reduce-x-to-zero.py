class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        target=sum(nums)-x
        if target<0:
            return -1

        l=0
        cnt=-1
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>target:
                curr-=nums[l]
                l+=1
            if curr==target:
                cnt=max(cnt,r-l+1)
        if cnt==-1:
            return -1
  
        return len(nums)-cnt

        

        
        