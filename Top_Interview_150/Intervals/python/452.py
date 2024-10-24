from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        right = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > right:
                count += 1
                right = points[i][1]

        return count


solution = Solution()
print(solution.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
