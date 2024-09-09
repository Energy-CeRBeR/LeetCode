from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        base_mx = max(candies)
        result = list(map(lambda x: x + extraCandies >= base_mx, candies))
        return result
