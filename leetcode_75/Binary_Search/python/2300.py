from typing import List


class Solution:

    @staticmethod
    def check_lower(arr, coeff, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] * coeff >= target:
                right = mid - 1
            else:
                left = mid + 1

        return len(arr) - left

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        result = [self.check_lower(potions, spells[i], success) for i in range(len(spells))]
        return result
