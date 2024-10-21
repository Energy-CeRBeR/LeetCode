from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        if n == 0:
            return [newInterval]

        new_intervals: List[List[int]] = []

        ptr = 0
        while ptr < n and intervals[ptr][0] < newInterval[0]:
            new_intervals.append(intervals[ptr])
            ptr += 1

        if new_intervals and new_intervals[-1][1] >= newInterval[0]:
            new_intervals[-1][1] = max(new_intervals[-1][1], newInterval[1])
        else:
            new_intervals.append(newInterval)

        while ptr < n:
            if intervals[ptr][0] > new_intervals[-1][1]:
                new_intervals.append(intervals[ptr])
            else:
                new_intervals[-1][1] = max(new_intervals[-1][1], intervals[ptr][1])
            ptr += 1

        return new_intervals


solution = Solution()
print(solution.insert([[1, 5]], [1, 7]))
