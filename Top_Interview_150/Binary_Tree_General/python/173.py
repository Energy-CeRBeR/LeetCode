from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def fill_stack(self, node: TreeNode):
        if node is None:
            return []

        self.fill_stack(node.right)
        self.stack = self.stack + [node.val]
        self.fill_stack(node.left)

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = list()
        self.fill_stack(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
