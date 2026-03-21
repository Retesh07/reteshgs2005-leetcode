class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)

        inorder(root)
        self.idx = 0

    def next(self) -> int:
        val = self.arr[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)