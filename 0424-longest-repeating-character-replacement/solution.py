class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=defaultdict(int)
        l=0
        r=0
        res=0
        maxf=0
        for r in range(len(s)):
            m[s[r]]+=1
            
            maxf=max(maxf,m[s[r]])
            while (r-l+1)-maxf>k:
                m[s[l]]-=1
                l+=1
                
            res=max(res,r-l+1)
        return res


        