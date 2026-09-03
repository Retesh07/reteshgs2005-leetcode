class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp={}
        nums=[1]+nums+[1]

        def dfs(l,r):

            if l+1==r:
                return 0 
            if (l,r)  in dp:
                return dp[(l,r)]
            res=0
            for k in range(l+1,r):
                coins=(nums[l]*nums[k]*nums[r]+dfs(l,k)+dfs(k,r))

                res=max(res,coins)
            dp[(l,r)]=res
            return dp[(l,r)]


           

         
        return dfs(0,len(nums)-1)

      
        