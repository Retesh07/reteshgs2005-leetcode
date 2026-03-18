class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color=[0]*(len(graph))
       
        q=deque()


        for i in range(len(graph)):
            if color[i]!=0:
                continue
            color[i]=1
            q.append(i)
            
            while q:
                m=q.popleft()
                for pre in graph[m]:
                    if color[m]==color[pre]:
                        return False
                    elif color[pre]!=0:
                        continue
                    else:
                        color[pre]=-color[m]
                        q.append(pre)
        return True
        