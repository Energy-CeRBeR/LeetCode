from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return

        q1 = deque([root.left])
        q2 = deque([root.right])

        while q1 and q2:
            left = q1.popleft()
            right = q2.popleft()

            if not left and not right:
                continue

            if not left and right or not right and left or left.val != right.val:
                return False

            q1.append(left.left)
            q1.append(left.right)
            q2.append(right.right)
            q2.append(right.left)

        return True if not q1 and not q2 else False

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.isMirror(root, root)

#     def isMirror(self, t1, t2):
#         if t1 is None and t2 is None:
#             return True
#         if t1 is None or t2 is None:
#             return False

#         if t1.val != t2.val:
#             return False

#         return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
