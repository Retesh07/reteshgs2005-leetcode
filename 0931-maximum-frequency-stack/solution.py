class FreqStack:
    

    def __init__(self):
        self.s1=defaultdict(int)
        self.s2=defaultdict(list)
        self.maxfreq=0
        
        

    def push(self, val: int) -> None:
        f=self.s1[val]+1
        self.s1[val]=f
        if self.maxfreq<f:
            self.maxfreq=f
        self.s2[f].append(val)
        
        
        

    def pop(self) -> int:
        k=self.s2[self.maxfreq].pop()
        self.s1[k]-=1
        if not self.s2[self.maxfreq]:
            self.maxfreq-=1





        return k
        
    
        
        
            


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()