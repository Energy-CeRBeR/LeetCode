from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx_sum = -1000000000

        def dfs(node):

            if node == None:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            self.mx_sum = max(self.mx_sum, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)

        dfs(root)

        return self.mx_sum
