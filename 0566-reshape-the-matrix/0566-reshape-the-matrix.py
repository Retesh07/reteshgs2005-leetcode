class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row=len(mat)
        col=len(mat[0])
        ans=[[0 for _ in range(c)] for _ in range(r)]
        x=0
        y=0

        if row*col!=r*c:
            return mat
        for i in range(row):
            for j in range(col):
                ans[x][y]=mat[i][j]
                y+=1
                if y==c:
                    x+=1
                    y=0
        return ans
        