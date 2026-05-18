class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        sub=[]
        w=set(wordDict)

        def dfs(i):
            if i==len(s):
                res.append(" ".join(sub))
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in w:
                    sub.append(word)
                    dfs(j+1)
                    sub.pop()
        dfs(0)
        return res

            
        



        