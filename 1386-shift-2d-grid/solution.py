class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        
        

        row,col=len(grid),len(grid[0])
        k=k%(row*col)

        


        while k!=0:
            temp=grid[row-1][col-1]
            for i in range(row-1,-1,-1):
                for j in range(col-1,-1,-1):
                    if j==0:
                        grid[i][j]=grid[i-1][col-1]
                        continue
                    if i==0 and j==0:
                        break
                
                    
                    grid[i][j]=grid[i][j-1]
            grid[0][0]=temp
            
            k-=1

        return grid

                


        