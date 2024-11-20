from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def generate_neighbors(node):
            for i in range(len(node)):
                for g in ["A", "C", "G", "T"]:
                    if node[i] != g:
                        yield f"{node[:i]}{g}{node[i + 1:]}"

        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = set()
        while queue:
            node, length = queue.popleft()

            if node == endGene:
                return length

            if node in visited:
                continue

            visited.add(node)

            for new_node in generate_neighbors(node):
                if new_node not in visited and new_node in bank:
                    queue.append((new_node, length + 1))

        return -1
