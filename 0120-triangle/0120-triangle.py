class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        
        dp=[triangle[0][0]]


        for i in range(1,len(triangle)):
            newdp=[0]*(i+1)
            for j in range(i+1):
                if j==0:
                    newdp[j]=dp[j]+triangle[i][j]
                elif j==i:
                    newdp[j]=dp[j-1]+triangle[i][j]
                else:
                    newdp[j]=min(dp[j-1],dp[j])+triangle[i][j]
            dp=newdp
               
        
        print(dp)
    
        return min(dp)

            