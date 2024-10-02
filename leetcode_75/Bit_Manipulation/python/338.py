from typing import List


class Solution:

    @staticmethod
    def unit_counter(num):
        count = 0
        while num > 0:
            count += (num % 2 == 1)
            num //= 2
        return count

    def countBits(self, n: int) -> List[int]:
        return list(self.unit_counter(x) for x in range(n + 1))


# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n + 1)
#         offset = 1

#         for i in range(1, n + 1):
#             if offset * 2 == i:
#                 offset = i
#             dp[i] = 1 + dp[i - offset]

#         return dp
