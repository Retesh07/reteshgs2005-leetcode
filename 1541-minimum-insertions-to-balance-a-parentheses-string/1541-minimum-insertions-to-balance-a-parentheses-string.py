class Solution:
    def minInsertions(self, s: str) -> int:

        opens=0
        i=0
        ans=0
        while i<len(s):
            if s[i]=='(':
                opens+=1
                i+=1
            else:
                if i+1<len(s) and s[i+1]==")":
            
                    i+=2
                else:
                    ans+=1
                    i+=1
                if opens>0:
                    opens-=1
                else:
                    ans+=1
            
        if opens>0:
            ans+=2*opens
        return ans
                

        