class MedianFinder:
    import heapq
    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:

  
        if len(self.right) == 0 or num <= self.right[0]:
            heapq.heappush(self.left, -num) 
        else:
            heapq.heappush(self.right, num)


        
        if len(self.left) > len(self.right) + 1:
            curr = -heapq.heappop(self.left)
            heapq.heappush(self.right, curr)
        elif len(self.right) > len(self.left):
            curr = heapq.heappop(self.right)
            heapq.heappush(self.left, -curr)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
    
        else:
            return (-self.left[0])
      
            
        


