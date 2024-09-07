from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for ast in asteroids:
            cur = ast
            stack.append(cur)
            if len(stack) >= 2:
                prev = stack[-2]
                while cur < 0 and prev > 0:
                    if abs(cur) > abs(prev):
                        stack[-2] = cur
                        stack.pop()
                    elif abs(cur) == abs(prev):
                        stack.pop()
                        stack.pop()
                    else:
                        stack.pop()

                    if len(stack) < 2:
                        break

                    cur = stack[-1]
                    prev = stack[-2]

        return list(stack)
