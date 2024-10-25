from typing import List


class Solution:

    def check_answer(self, nums, target, k):
        s = 0
        for i in range(k):
            s += nums[i]

        if s >= target:
            return True

        for i in range(k, self.n):
            s -= nums[i - k]
            s += nums[i]

            if s >= target:
                return True

        return False

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.n = len(nums)

        left = 0
        right = self.n
        while left <= right:
            middle = (left + right) // 2
            if self.check_answer(nums, target, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left if left <= self.n else 0
