class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1

        for j in range(len(nums)):
            newset=defaultdict(int)

            for i,count in dp.items():
                newset[i+nums[j]]+=count
                newset[i-nums[j]]+=count
            dp=newset
        return dp[target]

        