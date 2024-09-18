from typing import List


class Solution:
    def dfs(self, node, graph, visited):
        visited[node] = True
        for v in graph[node]:
            if not visited[v]:
                self.dfs(v, graph, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {i: set() for i in range(1, n + 1)}
        for i in range(1, n + 1):
            for j in range(1, len(isConnected[i - 1]) + 1):
                if isConnected[i - 1][j - 1] and i != j:
                    graph[i].add(j)
                    graph[j].add(i)

        visited = [False] * (n + 1)
        count = 0
        for i in range(1, n + 1):
            if not visited[i]:
                self.dfs(i, graph, visited)
                count += 1

        return count
