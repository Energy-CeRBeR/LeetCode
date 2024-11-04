from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_list(self, node: Optional[TreeNode]) -> List[Optional[int]]:
        if node is None:
            return [None]
        return [node.val] + self.get_list(node.left) + self.get_list(node.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.get_list(p) == self.get_list(q)


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
