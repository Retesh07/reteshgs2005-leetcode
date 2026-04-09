class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=[]

        while columnNumber:
            columnNumber-=1
            n= columnNumber%26
            ans.append(chr(n+ord('A')))
            columnNumber=columnNumber//26
        return ("").join(reversed(ans))
        