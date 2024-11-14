from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def tree_to_lst(node: Optional[TreeNode], lst):
            if node is None:
                return []

            return tree_to_lst(node.left, lst) + lst + [node.val] + tree_to_lst(node.right, lst)

        lst_tree = tree_to_lst(root, [])

        return lst_tree[k - 1]
