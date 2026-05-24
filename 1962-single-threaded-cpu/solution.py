class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])
        res,available=[],[]
        time,i=tasks[0][0],0

        while available or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(available,[tasks[i][1],tasks[i][2]])
                i+=1
            if available:
                processing_time,indx=heapq.heappop(available)
                time+=processing_time
                res.append(indx)
            else:
                time=tasks[i][0]
        return res
            
        
        