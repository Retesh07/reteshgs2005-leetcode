# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result=0
        def dia(curr):
            if not curr:
                return 0
            vl=dia(curr.left)
            vr=dia(curr.right)
            self.result=max(self.result,vl+vr)
            return 1+max(vl,vr)
        dia(root)

        return self.result
        