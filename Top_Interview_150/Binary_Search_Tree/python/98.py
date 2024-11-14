from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_val = float("-inf")

        def inorder(node: Optional[TreeNode]):
            if node is None:
                return True

            if not (inorder(node.left) and self.prev_val < node.val):
                return False
            self.prev_val = node.val

            return inorder(node.right)

        return inorder(root)


# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def valid(node, minimum, maximum):
#             if not node:
#                 return True

#             if not (node.val > minimum and node.val < maximum):
#                 return False

#             return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

#         return valid(root, float("-inf"), float("inf"))
