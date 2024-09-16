from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = [-10 ** 6, 0]
        q = deque([root])
        k = 0
        while q:
            k += 1
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if s > result[0]:
                result[0] = s
                result[1] = k

        return result[1]
