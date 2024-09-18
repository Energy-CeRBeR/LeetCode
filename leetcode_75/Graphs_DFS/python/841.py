from typing import List


class Solution:

    def dfs(self, node, graph, visited):
        visited[node] = True
        for v in graph[node]:
            if not visited[v]:
                self.dfs(v, graph, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = dict()
        for i in range(len(rooms)):
            graph[i] = rooms[i]

        visited = [False] * len(graph)
        visited[0] = True
        root = 0
        self.dfs(root, graph, visited)

        return True if all(x for x in visited) else False
