# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return []
        output=[]
        
        def dfs(node):
            if not node:
                return None
            output.append(node)
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        j=1
        
        for i in range(len(output)-1):
            output[i].right=output[j]
            output[i].left=None
            j+=1
        output[-1].left=None
        output[-1].right=None
        
        

        