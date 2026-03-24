# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append((root,0))
        maxi=0

       

        while q:
            left=q[0][1]
            right=q[-1][1]
            maxi=max(maxi,(right-left+1))

            for _ in range(len(q)):

                m,v=q.popleft()
                if m.left:
                    q.append((m.left,2*v+1))
                if m.right:
                    q.append((m.right,2*v+2))
            

        return maxi
                    
                    

            

            

        