from collections import deque
from typing import List


class Solution:

    def bfs(self, q: deque, graph: list, visited: set):
        count = 0
        while q:
            i, j, m = q.popleft()
            graph[i][j] = 2
            visited.add((i, j))

            flag = 0
            if 0 <= i - 1 < self.n and graph[i - 1][j] == 1 and (i - 1, j) not in visited:
                graph[i - 1][j] = 2
                flag = 1
                q.append((i - 1, j, m + 1))

            if 0 <= i + 1 < self.n and graph[i + 1][j] == 1 and (i + 1, j) not in visited:
                graph[i + 1][j] = 2
                flag = 1
                q.append((i + 1, j, m + 1))

            if 0 <= j - 1 < self.m and graph[i][j - 1] == 1 and (i, j - 1) not in visited:
                graph[i][j - 1] = 2
                flag = 1
                q.append((i, j - 1, m + 1))

            if 0 <= j + 1 < self.m and graph[i][j + 1] == 1 and (i, j + 1) not in visited:
                graph[i][j + 1] = 2
                flag = 1
                q.append((i, j + 1, m + 1))

            count = max(count, m + flag)

        return count

    def get_roots(self, grid):
        roots = deque([])
        good_counter = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    good_counter += 1
                if grid[i][j] == 2:
                    roots.append((i, j, 0))

        return roots, good_counter

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        q, good_counter = self.get_roots(grid)
        if len(q) == 0:
            return 0 if good_counter == 0 else -1

        visited = set()
        result = self.bfs(q, grid, visited)

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    return -1
        return result
