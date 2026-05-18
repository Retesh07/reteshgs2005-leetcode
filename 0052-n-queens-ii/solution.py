class Solution:
    def totalNQueens(self, n: int) -> int:
        if n>9:
            return 0
        res=[]
        board =[["."] * n for _ in range(n)]
      
        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if self.issafe(r,c,board,n):
                    board[r][c]='Q'
                    backtrack(r+1)
                    board[r][c]='.'
        backtrack(0)
        return len(res)

    def issafe(self,r,c,board,n):
        row=r-1
        while row>=0:
            if board[row][c]=='Q':
                return False
            row-=1
        row=r-1
        col=c-1
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=r-1
        col=c+1
        while row>=0 and col<n:
            if board[row][col]=='Q':
                return False
            row-=1
            col+=1
        return True

            


                    



        
        