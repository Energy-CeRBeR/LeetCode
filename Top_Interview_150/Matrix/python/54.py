from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        result = list()
        i = left = 0
        j = -1
        up = 1
        right = n
        down = m
        while len(result) < m * n:
            j += 1
            while len(result) < m * n and j < right:
                result.append(matrix[i][j])
                j += 1
            j -= 1
            right -= 1

            i += 1
            while len(result) < m * n and i < down:
                result.append(matrix[i][j])
                i += 1
            i -= 1
            down -= 1

            j -= 1
            while len(result) < m * n and j >= left:
                result.append(matrix[i][j])
                j -= 1
            j += 1
            left += 1

            i -= 1
            while len(result) < m * n and i >= up:
                result.append(matrix[i][j])
                i -= 1
            i += 1
            up += 1

        return result
