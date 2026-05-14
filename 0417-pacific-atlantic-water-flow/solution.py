class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row,col=len(heights),len(heights[0])
        pacific=set()
        atlantic=set()

        def dfs(r,c,visited):
            visited.add((r,c))
            directions=[(1,0),(-1,0),(0,1),(0,-1)]

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and heights[r][c]<=heights[nr][nc]:
                    
                    dfs(nr,nc,visited)




        for c in range(col):
            dfs(0,c,pacific)
            dfs(row-1,c,atlantic)
        for r in range(row):
            dfs(r,0,pacific)
            dfs(r,col-1,atlantic)

        res=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res


        