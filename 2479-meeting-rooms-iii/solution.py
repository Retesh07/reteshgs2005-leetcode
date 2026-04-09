class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available=[i for i in range(n)]
        busy=[]
        cnt=[0]*(n)

        for start,end in meetings:
            while busy and start>=busy[0][0]:
                finshedtime,room=heapq.heappop(busy)
                heapq.heappush(available,room)
            duration = end-start
            if available:
                r=heapq.heappop(available)
                heapq.heappush(busy,(end,r))
                cnt[r]+=1
            else:
                f,ro = heapq.heappop(busy)
                newend=duration+f
                heapq.heappush(busy,(newend,ro))
                cnt[ro]+=1
      
        
        return cnt.index(max(cnt))

        