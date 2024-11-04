from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return TreeNode(-101)

        left = self.isSymmetric(root.left)
        right = self.isSymmetric(root.right)

        return left.val == right.val
