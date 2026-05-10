class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dp = [[0] * 2 for _ in range(n)] # top two heights for each node

        def dfs(node, parent):
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                curHgt = 1 + dp[nei][0]
                if curHgt > dp[node][0]:
                    dp[node][1] = dp[node][0]
                    dp[node][0] = curHgt
                elif curHgt > dp[node][1]:
                    dp[node][1] = curHgt

        def dfs1(node, parent, topHgt):
            if topHgt > dp[node][0]:
                dp[node][1] = dp[node][0]
                dp[node][0] = topHgt
            elif topHgt > dp[node][1]:
                dp[node][1] = topHgt

            for nei in adj[node]:
                if nei == parent:
                    continue
                toChild = 1 + (dp[node][1] if dp[node][0] == 1 + dp[nei][0] else dp[node][0])
                dfs1(nei, node, toChild)

        dfs(0, -1)
        dfs1(0, -1, 0)

        minHgt, res = n, []
        for i in range(n):
            minHgt = min(minHgt, dp[i][0])
        for i in range(n):
            if minHgt == dp[i][0]:
                res.append(i)
        return res