class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False

            if graph[course] == []:
                if course not in res:
                    res.append(course)
                return True

            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)

            graph[course] = []      
            res.append(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res