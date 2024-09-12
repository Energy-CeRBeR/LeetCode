from typing import Optional
from functools import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @lru_cache(None)
    def get_leaves(self, node: TreeNode):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.get_leaves(node.left) + self.get_leaves(node.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)
