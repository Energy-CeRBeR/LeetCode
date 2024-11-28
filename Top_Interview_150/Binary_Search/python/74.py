from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left < right:
            middle = (left + right) // 2
            if matrix[middle][-1] == target:
                return True

            if matrix[middle][-1] < target:
                left = middle + 1
            else:
                if matrix[middle][0] <= target:
                    right = middle
                else:
                    right = middle - 1

        nums = matrix[left]
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return True

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False
