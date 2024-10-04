from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))

        right = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                right = intervals[i][1]
            else:
                count += 1

        return count
