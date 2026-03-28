class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m=int(pow(c,0.5))

        arr=[] #[0,1,2]
        for i in range(m+1):
            arr.append(i)
        l=0
        r=len(arr)-1

        while l<=r:
            a2=pow(arr[l],2)
            b2=pow(arr[r],2)

            if a2+b2==c:
                return True
            if a2+b2<c:
                l+=1
            else:
                r-=1
        return False
            

        