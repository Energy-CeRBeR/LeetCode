from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_sum = nums[0]
        cur_max = 0
        for num in nums:
            if cur_max < 0:
                cur_max = 0
            cur_max += num
            mx_sum = max(mx_sum, cur_max)

        return mx_sum
