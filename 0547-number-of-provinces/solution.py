class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited=set()
        n=len(isConnected)
        provinces=0

        def dfs(node):
           
            visited.add(node)
            for neigh in range(n):
                if isConnected[node][neigh]==1 and neigh not in visited:
                    dfs(neigh)



        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces+=1
        return provinces
        