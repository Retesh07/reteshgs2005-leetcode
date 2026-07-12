class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        c=[0]*26
        for i in range(len(s)):
            c[ord(s[i])-ord('a')]+=1
            c[ord(t[i])-ord('a')]-=1

        for value in c:
            if value!=0:
                return False
        return True
            
        