from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        ps = 0
        for i in range(len(nums)):
            if ps == s - ps - nums[i]:
                return i
            ps += nums[i]

        return -1
