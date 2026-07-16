class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        row = -1
        for i in range(m):
            if target <= matrix[i][n-1]:
                row = i
                break
        
        if row == -1:
            return False
        
        for j in range(n):
            if matrix[row][j] == target:
                return True
        
        return False
