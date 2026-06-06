# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        def r(curr,level):
            if not curr:
                return 
            if level==len(output):
                output.append(curr.val)
            r(curr.right,level+1)
            r(curr.left,level+1)
        r(root,0)
        return output
            
        
        

        