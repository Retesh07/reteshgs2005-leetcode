class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        scores=([0] * (n+1))
        for a,b in trust:
            scores[a]-=1
            scores[b]+=1
        for j in range(1,n+1):
            if scores[j]==n-1:
                return j
        return -1
        

        
        

