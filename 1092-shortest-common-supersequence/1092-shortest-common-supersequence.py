class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        t1=str1
        t2=str2
        dp=[[0 for _ in range(len(t2)+1)] for _ in range(len(t1)+1)]
        for i in range(1,len(t1)+1):

            for j in range(1,len(t2)+1):
                if t1[i-1]==t2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        

        k,l=len(str1),len(str2)
        res=""

        while k>0 and l>0:
            if str1[k-1]==str2[l-1]:
                res+=str1[k-1]
                k-=1
                l-=1
            elif dp[k-1][l]>dp[k][l-1]:
                res+=str1[k-1]
                k-=1
            else:
                res+=str2[l-1]
                l-=1
        while k>0:
            res+=str1[k-1]
            k-=1
        while l>0:
            res+=str2[l-1]
            l-=1
        return res[::-1]

        
        