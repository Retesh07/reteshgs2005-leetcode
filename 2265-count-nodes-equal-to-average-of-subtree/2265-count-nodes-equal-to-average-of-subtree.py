# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0

        def dfs(node):
            if node is None:
                return (0,0)
            leftsum,leftcount=dfs(node.left)
            rightsum,rightcount=dfs(node.right)

            totalsum=leftsum+rightsum+node.val
            totalcount=leftcount+rightcount+1
            avg=totalsum//totalcount
            if avg==node.val:
                self.count+=1
            return (totalsum,totalcount)
        dfs(root)
        return self.count


        