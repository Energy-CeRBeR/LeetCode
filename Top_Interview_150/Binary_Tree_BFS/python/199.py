from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()

        q = deque([])
        if root:
            q.append(root)

        while q:
            result.append(q[-1].val)

            level_length = len(q)
            for _ in range(level_length):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return result
