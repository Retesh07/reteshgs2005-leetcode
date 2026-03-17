# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q=deque()
        q.append((float('-inf'),root,float('inf')))

        while q:
            
            l,m,r=q.popleft()
            if not l<m.val<r:
                return False
            if m.left:
    
                q.append((l,m.left,m.val))

            if m.right:
                
                q.append((m.val,m.right,r))
             
        return True
                    

        