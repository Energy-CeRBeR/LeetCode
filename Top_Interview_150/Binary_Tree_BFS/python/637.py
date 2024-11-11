from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = list()

        q = deque([root])
        while q:
            level_length = len(q)
            level_sum = 0
            for _ in range(level_length):
                node = q.popleft()
                level_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            averages.append(level_sum / level_length)

        return averages
