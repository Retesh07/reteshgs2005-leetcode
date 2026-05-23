class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carpass=[0]*1001
        for t in trips:
            numpass,f,d=t
            carpass[f]+=numpass
            carpass[d]-=numpass
        currpass=0
        for i in range(1001):
            currpass+=carpass[i]
            if currpass>capacity:
                return False
        return True


        



        