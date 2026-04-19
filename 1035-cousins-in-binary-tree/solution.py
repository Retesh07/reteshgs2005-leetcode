from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])

        while q:
            found_x = found_y = False

            for _ in range(len(q)):
                node = q.popleft()

                # Check if x and y are siblings
                if node.left and node.right:
                    if {node.left.val, node.right.val} == {x, y}:
                        return False

                if node.val == x:
                    found_x = True
                if node.val == y:
                    found_y = True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if found_x and found_y:
                return True

            if found_x or found_y:
                return False

        return False