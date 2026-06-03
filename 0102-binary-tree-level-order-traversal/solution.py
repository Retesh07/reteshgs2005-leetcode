# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        output=[]
        q=collections.deque()
        q.append(root)
        while q:
            qL=len(q)
            level=[]
            for _ in range(qL):
                m=q.popleft()
                level.append(m.val)
                if m.left:
                    q.append(m.left)
                if m.right:
                    q.append(m.right)
            output.append(level)
        return output

        
        


        