from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        for n in set(nums):
            d[n] = d[n - 1] + 1 if n - 1 in d else 1
            k = n + 1
            while k in d:
                d[k] = d[k - 1] + 1
                k += 1

        return max(d.values()) if d else 0
