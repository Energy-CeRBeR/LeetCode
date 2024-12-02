from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        init_pos = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                init_pos = middle
                break

            elif nums[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        if init_pos == -1:
            return [-1, -1]

        old_right = right
        start_pos = init_pos
        right = init_pos
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                start_pos = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        end_pos = init_pos
        right = old_right
        left = init_pos
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                end_pos = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return [start_pos, end_pos]
