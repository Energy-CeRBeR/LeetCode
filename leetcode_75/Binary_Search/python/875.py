from typing import List


class Solution:

    def check_answer(self, k, piles, h):
        s = 0
        for pile in piles:
            s += pile // k + (pile % k != 0)

        return True if h >= s else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10 ** 9
        while left <= right:
            mid = (left + right) // 2
            if self.check_answer(mid, piles, h):
                right = mid - 1
            else:
                left = mid + 1

        return left
