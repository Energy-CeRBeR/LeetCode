from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    targetSum = 0

    def get_sum(self, node: TreeNode, s: int):
        if node is None:
            return 0

        s += node.val
        return int(s == self.targetSum) + self.get_sum(node.left, s) + self.get_sum(node.right, s)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum

        def wrapper(node: TreeNode):

            if node is None:
                return 0

            return self.get_sum(node, 0) + wrapper(node.left) + wrapper(node.right)

        return wrapper(root)