class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        for k in range(0,len(s)//2):
            s[k],s[j]=s[j],s[k]
            j-=1
        return s

        