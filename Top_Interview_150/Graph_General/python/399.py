from collections import defaultdict, deque
from typing import List


class Solution:

    @staticmethod
    def bfs(start, end, graph) -> float:
        queue = deque([(start, 1)])
        visited = set()
        while queue:
            node, res = queue.popleft()

            if node in visited:
                continue

            if node == end:
                return res

            visited.add(node)
            for neighbour, coeff in graph[node]:
                queue.append((neighbour, res * coeff))

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        for i in range(len(equations)):
            graph[equations[i][0]].add((equations[i][1], values[i]))
            graph[equations[i][1]].add((equations[i][0], 1 / values[i]))

        response = []
        for query in queries:
            start, end = query
            if start not in graph or end not in graph:
                response.append(-1)
            else:
                response.append(self.bfs(start, end, graph))

        return response


solution = Solution()
print(solution.calcEquation(equations=[["a", "b"], ["c", "d"]], values=[
      1.0, 1.0], queries=[["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]))
