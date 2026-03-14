class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minheap=[]
        for num in nums:
            heapq.heappush(minheap,num)
            while len(minheap)>2:
                heapq.heappop(minheap)
        return ((minheap[0]-1) * (minheap[1]-1))
    

        