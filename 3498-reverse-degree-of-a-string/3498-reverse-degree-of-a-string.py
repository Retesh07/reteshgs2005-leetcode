class Solution:
    def reverseDegree(self, s: str) -> int:

        sums=0
        

        for i in range(1,len(s)+1):
            print(i,ord('z')-ord(s[i-1])+1)
            sums+=(i*(ord('z')-ord(s[i-1])+1))
            
        return sums

        