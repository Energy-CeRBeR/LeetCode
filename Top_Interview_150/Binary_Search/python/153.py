from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)

        left = 0
        right = length - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[-1]:
                left = middle + 1
            else:
                right = middle - 1

        return nums[left]
