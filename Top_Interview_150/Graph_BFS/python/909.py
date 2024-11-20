from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def get_pos(cur_pos):
            r = (cur_pos - 1) // n
            c = (cur_pos - 1) % n

            if r % 2:
                c = n - 1 - c

            return [r, c]

        q = deque([(1, 0)])
        visited = set()
        while q:
            node, moves = q.popleft()

            for i in range(1, 7):
                next_node = node + i
                r, c = get_pos(next_node)

                if board[r][c] != -1:
                    next_node = board[r][c]

                if next_node == n * n:
                    return moves + 1

                if next_node not in visited:
                    visited.add(next_node)
                    q.append((next_node, moves + 1))

        return -1
