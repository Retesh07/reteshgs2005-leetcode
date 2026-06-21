class MinStack:
    

    def __init__(self):
        self.s1=[]
        self.s2=[]
        
        

    def push(self, val: int) -> None:
        self.s1.append(val)
        v1=min(val, self.s2[-1] if self.s2 else val)
        self.s2.append(v1)

        
        

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()

        
        

    def top(self) -> int:
        return self.s1[-1]
        
        

    def getMin(self) -> int:
        return self.s2[-1]
        
