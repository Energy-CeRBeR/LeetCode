from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []

        left = nums[0]
        result = []
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                if left == nums[i - 1]:
                    result.append(str(left))
                else:
                    result.append(f"{left}->{nums[i - 1]}")
                left = nums[i]

        if left == nums[n - 1]:
            result.append(str(nums[n - 1]))
        else:
            result.append(f"{left}->{nums[n - 1]}")

        return result
