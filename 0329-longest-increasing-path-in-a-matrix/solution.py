class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            best = 1 
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and matrix[ni][nj] > matrix[i][j]
                ):
                    best = max(best, 1 + dfs(ni, nj))

            memo[(i, j)] = best
            return best

        ans = 0

        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans