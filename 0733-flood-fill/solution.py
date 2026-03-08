class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        q=deque()
        oldcolor=image[sr][sc]
        q.append((sr,sc))
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        row,col=len(image),len(image[0])
        visited=set()

        while len(q):
            r,c=q.popleft()
            visited.add((r,c))
            image[r][c]=color
            
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=row or nc>=col or (nr,nc) in visited:
                    continue
                if image[nr][nc]==oldcolor:
                    
                    q.append((nr,nc))
        return image


        
        