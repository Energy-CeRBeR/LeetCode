from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()

        q = deque([])
        if root:
            q.append(root)

        while q:
            level_length = len(q)
            level_data = []
            for _ in range(level_length):
                node = q.popleft()
                level_data.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            result.append(level_data)

        return result
