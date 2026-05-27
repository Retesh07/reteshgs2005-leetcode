class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap=[0]*len(stones)
 
        for i in range(len(stones)):
            minheap[i]=-(stones[i])

        heapq.heapify(minheap)
        while len(minheap)>1:

            p=heapq.heappop(minheap)
            q=heapq.heappop(minheap)
            y=-p
            x=-q
            

            if y>x:
             heapq.heappush(minheap,-(y-x))
        if minheap:

            return -(minheap[0])
        return 0
    
        