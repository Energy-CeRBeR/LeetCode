from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        strings = dict()
        for line in grid:
            hashable_line = tuple(line)
            if hashable_line not in strings:
                strings[hashable_line] = 0
            strings[hashable_line] += 1

        counter = 0
        for i in range(n):
            cur_column = list()
            for j in range(n):
                cur_column.append(grid[j][i])
            hashable_column = tuple(cur_column)
            if hashable_column in strings:
                counter += strings[hashable_column]

        return counter
