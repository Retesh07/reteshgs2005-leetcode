
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q1 = deque([root.left])
        q2 = deque([root.right])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            q1.append(n1.left)
            q1.append(n1.right)

            q2.append(n2.right)
            q2.append(n2.left)

        return len(q1) == len(q2)