class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap = [[] for i in range(numCourses)]
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        res=[]
       

        def dfs(start,end,visited):
            visited.add(start)
            if start==end:
                return True
            for preq in preMap[start]:
                if preq not in visited:
                    if dfs(preq,end,visited):
                        return True
            return False
     


        

        for u,v in queries:
            if not dfs(u,v,set()):
                res.append(False)
            else:
                res.append(True)
        return res

        