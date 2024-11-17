from collections import defaultdict
from typing import List


class Solution:

    def dfs(self, node, visited, graph):
        if node not in visited:
            visited.add(node)
            self.flag = True

        visited.add(node)
        for v in graph[node]:
            if v not in visited:
                self.dfs(v, visited, graph)

    def validate_pos(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        land_lst = list()

        graph = defaultdict(set)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    land_lst.append((i, j))

                    if self.validate_pos(i + 1, j) and grid[i + 1][j] == '1':
                        graph[(i, j)].add((i + 1, j))
                        graph[(i + 1, j)].add((i, j))
                    if self.validate_pos(i - 1, j) and grid[i - 1][j] == '1':
                        graph[(i, j)].add((i - 1, j))
                        graph[(i - 1, j)].add((i, j))
                    if self.validate_pos(i, j + 1) and grid[i][j + 1] == '1':
                        graph[(i, j)].add((i, j + 1))
                        graph[(i, j + 1)].add((i, j))
                    if self.validate_pos(i, j - 1) and grid[i][j - 1] == '1':
                        graph[(i, j)].add((i, j - 1))
                        graph[(i, j - 1)].add((i, j))

        visited = set()
        count = 0
        for pos in land_lst:
            self.flag = False
            self.dfs(pos, visited, graph)

            if self.flag:
                count += 1

        return count


solution = Solution()
print(solution.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
