class Solution:
    def maxProduct(self, n: int) -> int:
        m=str(n)
        res=[]

        for i in range(len(m)):
            res.append(-int(m[i]))
        heapq.heapify(res)
        p1=-heapq.heappop(res)
        p2=-heapq.heappop(res)

        return p1*p2
        