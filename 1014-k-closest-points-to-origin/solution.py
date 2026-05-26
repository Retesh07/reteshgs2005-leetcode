class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            dist=x*x+y*y
            heapq.heappush(minheap,(dist,[x,y]))
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(minheap)[1])
        return ans





        