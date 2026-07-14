class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        l1=len(g)
        l2=len(s)
        child=0
        cookie=0
        while child<l1 and cookie<l2:
            if s[cookie]>=g[child]:
                child+=1
            cookie+=1
        return child
    
        
        