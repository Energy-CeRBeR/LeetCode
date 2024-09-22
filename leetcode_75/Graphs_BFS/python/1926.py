from collections import deque
from typing import List


class Solution:

    INF = 10 ** 4

    def bfs(self, q: deque, graph: dict, dist: dict):
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == self.INF:
                    q.append(neighbor)
                    dist[neighbor] = min(dist[neighbor], dist[node] + 1)

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        graph = dict()
        dist = dict()
        exits = set()

        for i in range(n):
            for j in range(m):
                if maze[i][j] == ".":
                    dist[(i, j)] = self.INF
                    graph[(i, j)] = set()

                    if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                        exits.add((i, j))

                    if i - 1 >= 0 and maze[i - 1][j] == ".":
                        graph[(i, j)].add((i - 1, j))
                    if i + 1 < n and maze[i + 1][j] == ".":
                        graph[(i, j)].add((i + 1, j))
                    if j - 1 >= 0 and maze[i][j - 1] == ".":
                        graph[(i, j)].add((i, j - 1))
                    if j + 1 < m and maze[i][j + 1] == ".":
                        graph[(i, j)].add((i, j + 1))

        root = tuple(entrance)
        dist[root] = 0
        q = deque([root])

        self.bfs(q, graph, dist)

        mn = self.INF
        for pos in exits:
            d = dist.get(pos, self.INF)
            if d != 0:
                mn = min(mn, d)

        if mn != self.INF:
            return mn
        else:
            return -1
