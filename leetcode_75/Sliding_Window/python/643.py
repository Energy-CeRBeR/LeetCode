from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_s = 0
        for i in range(k):
            cur_s += nums[i]
        mx_sum = cur_s

        for i in range(k, len(nums)):
            cur_s += nums[i] - nums[i - k]
            mx_sum = max(mx_sum, cur_s)

        return mx_sum / k
