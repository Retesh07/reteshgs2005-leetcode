class StockSpanner:

    def __init__(self):
        self.s1=[]
        
        

    def next(self, price: int) -> int:
        span=1
        while self.s1 and self.s1[-1][0]<=price:
                span+=self.s1[-1][1]
                self.s1.pop()
        self.s1.append([price,span])
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)