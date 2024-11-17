from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        head = Node(node.val)

        queue = deque([node])
        new_node = head
        new_queue = deque([new_node])
        visited = {node.val: new_node}

        while queue:
            cur_node = queue.popleft()
            new_node = new_queue.popleft()

            for neighbor in cur_node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    new_neighbor = Node(neighbor.val)
                    new_queue.append(new_neighbor)
                    visited[neighbor.val] = new_neighbor

                else:
                    new_neighbor = visited[neighbor.val]

                new_node.neighbors.append(new_neighbor)

        return head
