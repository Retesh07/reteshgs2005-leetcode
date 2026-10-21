class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        sorteds=True
        for i in range(1,n):
            if s[i]<s[i-1]:
                sorteds=False
                break
        if sorteds:
            return 0
        if n==2:
            return -1
        m=min(s)
        k=max(s)
        if s[0]==m or s[-1]==k:
            return 1
        for j in s[1:-1]:
            if j==m or j==k:
                return 2
        return 3



        
        