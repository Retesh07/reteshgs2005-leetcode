# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append((root,0))
        output=[]
        if not root:
            return []

        while q:
            size=len(q)
            level=[0]*(size)
            j=0
            for i in range(size):
                m,lev=q.popleft()
                if lev%2==0:
                    level[j]=m.val
                    j+=1
                else:
                    level[size-j-1]=m.val
                    j+=1
                if m.left:
                    q.append((m.left,lev+1))
                if m.right:
                    q.append((m.right,lev+1))
            output.append(level)
        return output
            
                
        