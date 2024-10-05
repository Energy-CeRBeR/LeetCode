from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = [(temperatures[0], 0)]
        for i in range(1, n):
            while stack and stack[-1][0] < temperatures[i]:
                data = stack.pop()
                result[data[1]] = (i - data[1])

            stack.append((temperatures[i], i))

        return result
