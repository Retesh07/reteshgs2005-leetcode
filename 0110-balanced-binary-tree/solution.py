# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.val=True

        def height_diff(curr):
            if not curr:
                return 0
            vl=height_diff(curr.left)
            if vl==-1:
                return -1
            vr=height_diff(curr.right)
            if vr==-1:
                return -1
            v3=abs(vr-vl)
            if v3>1:
                return -1
            return 1+max(vl,vr)
        
        return height_diff(root)!=-1
        