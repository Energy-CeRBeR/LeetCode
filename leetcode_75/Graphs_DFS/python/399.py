from typing import List


class Solution:

    def dfs(self, node, finish_node, graph, visited, data, result):
        if node in graph:
            visited[node] = True
            result *= data
            if node == finish_node:
                self.__cur_res = result
                return

            for v in graph[node]:
                if not visited[v[0]]:
                    self.dfs(v[0], finish_node, graph, visited, v[1], result)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        for i in range(len(values)):
            a, b = equations[i]
            val = values[i]

            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()

            graph[a].add((b, val))
            graph[b].add((a, 1 / val))

        response = list()
        for query in queries:
            self.__cur_res = -1
            start = query[0]
            finish = query[1]
            visited = {i: False for i in graph}
            self.dfs(start, finish, graph, visited, 1, 1)
            response.append(self.__cur_res)

        return response
