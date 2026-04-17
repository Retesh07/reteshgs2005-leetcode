class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1=len(word1)
        l2=len(word2)
        if l2==0:
            return l1
        if not l1 and not l2:
            return 0
        if not l1 and l2:
            return l2
        memo={}

        def dfs(i,j):
            if j==l2:
                return l1-i
            if i==l1:
                return l2-j
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)]=dfs(i+1,j+1)
            else:
                memo[(i,j)]=1+min(dfs(i,j+1) , dfs(i+1,j+1) , dfs(i+1,j))
            return memo[(i,j)]

        return dfs(0,0)
    



        