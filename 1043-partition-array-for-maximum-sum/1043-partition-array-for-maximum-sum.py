class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)

        dp=[0]*(n+1)
        dp[1]=arr[0]
        for i in range(2,n+1):
            mx=0

            for length in range(1,k+1):
                if i-length<0:
                    break
                ele=arr[i-length]
                mx=max(mx,ele)
                dp[i]=max(dp[i],dp[i-length]+mx*length)
        return dp[n]

        