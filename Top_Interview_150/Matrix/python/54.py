from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # if m == 1 or n == 1:
        #     return matrix

        count = 1
        i = 0 if m > 1 else 1
        j = 1 if m > 1 else 0
        height_step = line_step = 1
        result = matrix[0][0]

        flag = m > 1

        while count < m * n:
            if flag:
                j += line_step
                if j == 0 or j == n - 1:
                    flag = False
                    line_step = - line_step
            else:
                i += height_flag
