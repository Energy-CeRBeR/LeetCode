from typing import List


class Solution:

    @staticmethod
    def set_null_line(matrix, x, m):
        for i in range(m):
            matrix[x][i] = 0

    @staticmethod
    def set_null_column(matrix, y, n):
        for i in range(n):
            matrix[i][y] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])
        null_lines = set()
        null_columns = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    null_lines.add(i)
                    null_columns.add(j)

        for x in null_lines:
            self.set_null_line(matrix, x, m)

        for y in null_columns:
            self.set_null_column(matrix, y, n)
