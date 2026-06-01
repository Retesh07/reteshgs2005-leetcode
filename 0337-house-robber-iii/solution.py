# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0,0)
            leftrob,leftnot=dfs(node.left)
            rightrob,rightnot=dfs(node.right)

            rob=node.val+leftnot+rightnot
            notrob = max(leftrob,leftnot)+max(rightrob,rightnot)
            return(rob,notrob)
        return max(dfs(root))

        