class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row,col=len(mat),len(mat[0])

        l=0 
        r=col-1
        while l<=r:
            mid=(l+r)//2
            maxi=-1
            x=0
            for i in range(row):
                if maxi<mat[i][mid]:
                    maxi=mat[i][mid]
                    x=i
            left = -1 if mid == 0 else mat[x][mid - 1]
            right = -1 if mid == col - 1 else mat[x][mid + 1]
            current = mat[x][mid]
            if current>left and current>right:
                return [x,mid]
            elif current>left:
                l=mid+1
            else:
                r=mid-1
        return [0,0]
        
        