class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,m):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        p1=0
        p2=n-1
        for k in range(n):
            while(p1<p2):
                matrix[k][p1],matrix[k][p2] = matrix[k][p2],matrix[k][p1]
                p1=p1+1
                p2=p2-1
            p1=0
            p2=n-1

        
    

         




        

            

        