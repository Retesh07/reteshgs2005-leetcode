# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(p,maximum):
            c=0
        
            if not p:
                return 0
            if p.val>=maximum:
                c=1
                maximum=p.val
            c+=dfs(p.left,maximum)
            c+=dfs(p.right,maximum)
            return c
        return dfs(root,root.val)



        