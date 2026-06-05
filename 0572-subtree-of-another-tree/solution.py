class Solution:
    def isSubtree(self, root, subRoot):
        def isSame(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return isSame(a.left, b.left) and isSame(a.right, b.right)

        if not root:
            return False

        if isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))