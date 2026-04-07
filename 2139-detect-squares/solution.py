class DetectSquares:

    def __init__(self):
        self.m=defaultdict(lambda:defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        p,q=point
        self.m[p][q]+=1
        

    def count(self, point: List[int]) -> int:
        res=0
        x,y=point
        if x not in self.m:
            return 0
        for ny,cnt in self.m[x].items():
            if ny==y:
                continue
            d=ny-y
            res+=(cnt*self.m[x+d][y]*self.m[x+d][ny])
            res+=(cnt*self.m[x-d][y]*self.m[x-d][ny])
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)