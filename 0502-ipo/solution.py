class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    
        l = []
        for i in range(len(profits)):
            l.append([capital[i],profits[i]])
        l.sort(key=lambda t : t[0])
        maxheap=[]
        i=0
        while k:
        
            while i<len(profits) and l[i][0]<=w:
                heapq.heappush(maxheap,-(l[i][1]))
                i+=1
            if not maxheap:
                break
            p=heapq.heappop(maxheap)
            w+=-(p)
            
            k-=1
        return w

            
            
            

