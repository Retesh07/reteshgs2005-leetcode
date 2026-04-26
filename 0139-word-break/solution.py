class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            if not dp[i]:
                continue
            for word in wordDict:
                j=i+len(word)
                w=s[i:j]
                if w == word:
                    if j<=n:
                        dp[j]=True
        return dp[n]
          
            
        

        
           
        

        