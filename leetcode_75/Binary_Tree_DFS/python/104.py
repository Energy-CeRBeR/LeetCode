from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def height(self, node: TreeNode):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)
