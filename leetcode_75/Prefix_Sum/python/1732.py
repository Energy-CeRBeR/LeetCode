from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_height = 0
        mx = 0
        for dh in gain:
            cur_height += dh
            mx = max(mx, cur_height)

        return mx
