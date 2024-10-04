from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        right = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > right:
                right = points[i][1]
                count += 1
            else:
                right = min(right, points[i][1])

        return count
