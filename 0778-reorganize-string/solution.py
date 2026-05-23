class Solution:
    def reorganizeString(self, s: str) -> str:
        c=Counter(s)
        maxheap=[[-cnt,m] for m,cnt in c.items()]
        heapq.heapify(maxheap)

        prev = None
        res=""
        

        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt,m = heapq.heappop(maxheap)
            res+=m
            cnt+=1
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None

            if cnt<0:
                
                prev = [cnt,m]
        return res

        