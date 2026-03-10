class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row,col=len(mat),len(mat[0])
    
        index=-1
        maxcount=-1
        for i in range(row):
            mat[i].sort()
            l=0
            r=col-1
            while l<=r:
                mid=(l+r)//2
                if mat[i][mid]==1:
                    r=mid-1
                else:
                    l=mid+1
            cnt=col-l
            print(cnt)
            if maxcount<cnt:
                maxcount=cnt
                index=i
        return [index,maxcount]
            

        