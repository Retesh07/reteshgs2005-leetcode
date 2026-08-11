
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        sizes={}
        island=2
        row,col=len(grid),len(grid[0])
        directions=[(0,1),(-1,0),(1,0),(0,-1)]
        for r in range(row):
            for c in range(col):
                if grid[r][c]!=1:
                    continue
                q=deque([(r,c)])
                grid[r][c]=island
                size=1

                while q:
                    nr,nc=q.popleft()
                    for dr,dc in directions:
                        newr,newc=nr+dr,nc+dc
                        if newr<0 or newc<0 or newr>=row or newc>=col or grid[newr][newc]!=1:
                            continue
                        grid[newr][newc]=island
                        q.append((newr,newc))
                        size+=1
                sizes[island]=size

                island+=1
                
        ans=max(sizes.values(),default=0)
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] != 0:
                    continue

                unique_islands = set()
                current_area = 1

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        island = grid[nr][nc]

                        if island > 1 and island not in unique_islands:
                            unique_islands.add(island)
                            current_area += sizes[island]

                ans = max(ans, current_area)

        return ans
                            





        