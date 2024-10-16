from typing import List
from copy import deepcopy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        base_matrix = deepcopy(matrix)

        for i in range(n):
            for j in range(m):
                matrix[i][j] = base_matrix[m - j - 1][i]


solution = Solution()
solution.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
