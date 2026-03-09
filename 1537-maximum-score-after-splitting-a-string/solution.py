class Solution:
    def maxScore(self, s: str) -> int:
        ones=0
        for i in range(len(s)):
            if s[i]=='1':
                ones+=1
        zeros=0
        total=float('-inf')
        for j in range(len(s)-1):
            if s[j]=='0':
                zeros+=1
            else:
                ones-=1
            total=max(total,ones+zeros)

        return total
        