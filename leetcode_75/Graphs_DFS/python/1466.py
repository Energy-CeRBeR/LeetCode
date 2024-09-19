from typing import List


class Solution:

    __count = 0

    def dfs(self, node, oriented_graph, base_graph, visited):
        visited[node] = True
        for v in oriented_graph[node]:
            if not visited[v]:
                if v in base_graph[node]:
                    self.__count += 1
                self.dfs(v, oriented_graph, base_graph, visited)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        base_graph = {i: set() for i in range(n)}
        oriented_graph = {i: set() for i in range(n)}

        for i in range(n - 1):
            base_graph[connections[i][0]].add(connections[i][1])
            oriented_graph[connections[i][0]].add(connections[i][1])
            oriented_graph[connections[i][1]].add(connections[i][0])

        root = 0
        visited = [False] * n
        visited[0] = True
        self.dfs(root, oriented_graph, base_graph, visited)

        return self.__count
