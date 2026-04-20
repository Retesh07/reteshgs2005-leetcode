class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}
        def dfs(i,a,b):
            if i==len(s3):
                return a==len(s1) and b==len(s2)
            if (i,a,b) in memo:
                return memo[(i,a,b)]
            ans1=False
            ans2=False
            if a<len(s1) and s3[i]==s1[a]:
                ans1=dfs(i+1,a+1,b)
            if b<len(s2) and s3[i]==s2[b]:
                ans2=dfs(i+1,a,b+1)
            memo[(i,a,b)] = ans1 or ans2
         
            return ans1 or ans2
        return dfs(0,0,0)
        
        