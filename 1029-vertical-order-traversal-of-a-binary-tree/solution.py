class Solution:
    def verticalTraversal(self, root):
        nodes = []

        def dfs(node, row, col):
            if not node:
                return

            nodes.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        nodes.sort()

        ans = []
        prev_col = None

        for col, row, val in nodes:
            if col != prev_col:
                ans.append([])
                prev_col = col

            ans[-1].append(val)

        return ans