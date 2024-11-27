from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        d = defaultdict(set)

        INF = 10 ** 9

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    d[(x1, INF)].add((tuple(points[i])))
                    d[(x1, INF)].add(tuple(points[j]))

                elif y2 == y1:
                    d[(INF, y1)].add((tuple(points[i])))
                    d[(INF, y1)].add(tuple(points[j]))
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                    d[(k, b)].add((tuple(points[i])))
                    d[(k, b)].add(tuple(points[j]))

        if d:
            return len(max(d.values(), key=len))
        else:
            return 1
