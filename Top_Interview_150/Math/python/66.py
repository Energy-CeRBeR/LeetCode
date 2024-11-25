from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        digits[i] += 1
        while digits[i] == 10 and i > 0:
            digits[i] = 0
            digits[i - 1] += 1
            i -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits


solution = Solution()
print(solution.plusOne([8, 8, 8]))
