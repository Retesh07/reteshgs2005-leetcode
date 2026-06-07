# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(curr1,curr2):
            if not curr1 and not curr2:
                return 0
            if not curr1 and curr2:
                return -1
            if curr1 and not curr2:
                return -1
            if curr1 and curr2:
                if curr1.val!=curr2.val:
                    return -1
            vl=same(curr1.left,curr2.left)
            if vl==-1:
                return -1
            
            vr=same(curr1.right,curr2.right)
            if vr==-1:
                return -1
            
        return same(p,q)!=-1
            
            
        