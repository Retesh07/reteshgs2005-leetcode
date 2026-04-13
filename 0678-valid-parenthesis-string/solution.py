class Solution:
    def checkValidString(self, s: str) -> bool:

        left,high=0,0

        for i in s:
            if i=='(':
                left,high = left+1,high+1
            elif i==')':
                left,high = left-1,high-1
            else:
                left,high=left-1,high+1
            if high<0:
                return False
            left=max(0,left)
        return left==0
        