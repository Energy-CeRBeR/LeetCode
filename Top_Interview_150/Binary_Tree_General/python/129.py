from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, str_num: str):
            if node is None:
                return 0

            str_num += str(node.val)

            if node.left is None and node.right is None:
                return int(str_num)

            return dfs(node.left, str_num) + dfs(node.right, str_num)

        return dfs(root, "")
