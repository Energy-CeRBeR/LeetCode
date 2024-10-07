from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0

        for i in range(n - 1):
            if i <= max_index:
                max_index = max(max_index, i + nums[i])

        return n - 1 <= max_index
