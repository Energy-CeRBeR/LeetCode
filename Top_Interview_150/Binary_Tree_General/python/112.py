from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check_sum(node: TreeNode, cur_s: int = 0):
            if node is None:
                return False

            cur_s += node.val

            if node.left is None and node.right is None:
                return cur_s == targetSum

            return check_sum(node.left, cur_s) or check_sum(node.right, cur_s)

        return check_sum(root)
