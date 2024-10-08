from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count = last = max_index = 0

        for i in range(len(nums) - 1):
            max_index = max(max_index, i + nums[i])

            if i == last:
                last = max_index
                count += 1

        return count
