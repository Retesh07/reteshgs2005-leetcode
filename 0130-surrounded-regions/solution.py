class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col=len(board),len(board[0])
        visited=set()

        def dfs(r,c):

            if r<0 or c<0 or r>=row or c>=col or (r,c) in visited or board[r][c]!="O":
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for c in range(col):
            if board[0][c]=="O":
                dfs(0,c)
            if board[row-1][c]=="O":
                dfs(row-1,c)
        for r in range(row):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][col-1]=="O":
                dfs(r,col-1)
        for k in range(row):
            for l in range(col):
                if board[k][l]=="O" and (k,l) not in visited:
                    board[k][l]="X"
        
            
        
        
            
        