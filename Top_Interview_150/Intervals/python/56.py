from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = []

        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] > right:
                result.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            else:
                right = max(right, intervals[i][1])

        result.append([left, right])

        return result
