class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited=set()
        q=deque()
        row,col=len(mat),len(mat[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))
        while q:
            r,c=q.popleft()
            
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr,nc) in visited or nr<0 or nc<0 or nr>=row or nc>=col:
                    continue
                mat[nr][nc]=mat[r][c]+1
                q.append((nr,nc))
                visited.add((nr,nc))
        return mat
                


        