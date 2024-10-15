from typing import List


class Solution:

    @staticmethod
    def add_elem(data: set, elem: str):
        cur_len = len(data)
        data.add(elem)

        return cur_len != len(data)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lines = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():

                    x1 = self.add_elem(lines[i], board[i][j])
                    x2 = self.add_elem(columns[j], board[i][j])
                    x3 = self.add_elem(blocks[i // 3][j // 3], board[i][j])

                    if not (x1 and x2 and x3):
                        return False

        return True


solution = Solution()
print(solution.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
