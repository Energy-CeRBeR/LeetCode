from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_mx_path(self, node: TreeNode, count: int, last_action: str):
        if node is None:
            return count
        
        count += 1
        if last_action == "left":
            return max(self.get_mx_path(node.right, count, "right"), self.get_mx_path(node.left, 0, "left"))
        else:
            return max(self.get_mx_path(node.left, count, "left"), self.get_mx_path(node.right, 0, "right"))

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.get_mx_path(root.left, 0, "left"), self.get_mx_path(root.right, 0, "right"))
