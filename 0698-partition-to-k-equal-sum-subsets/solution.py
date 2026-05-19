class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        target=sum(nums)//k
        subsets=[0]*k
        nums.sort(reverse=True)
        if nums[0]>target:
            return False

        def dfs(i):
            if i==len(nums):
                return True
            
            for s in range(k):
                if subsets[s]+nums[i]<=target:
                    subsets[s]+=nums[i]

                    if dfs(i+1):
                        return True
                    subsets[s]-=nums[i]
                if subsets[s]==0:
                    break
            return False
        return dfs(0)
            

        