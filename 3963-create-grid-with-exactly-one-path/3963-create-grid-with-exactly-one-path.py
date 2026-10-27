class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        ans=[]

        for i in range(m-1):
            k=""
            for j in range(n):
                if j==0:
                    k+='.'
                else:
                    k+='#'
            ans.append(k)
        h=""
        for m in range(n):
            h+='.'
        ans.append(h)
        return ans
        