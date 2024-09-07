from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)

        return "".join(i for i in stack)
