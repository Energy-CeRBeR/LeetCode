from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mn_diff = 1e9
        self.prev = None

        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            if self.prev != None:
                self.mn_diff = min(self.mn_diff, node.val - self.prev.val)
            self.prev = node

            dfs(node.right)

        dfs(root)

        return self.mn_diff
