from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        s = 0
        for x in nums:
            s += x
            d.add(x)

        return 2 * sum(d) - s
