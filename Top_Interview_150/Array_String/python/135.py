from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        if n == 1:
            return 1

        dp = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1

        count = dp[i]
        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                dp[i - 1] = max(dp[i - 1], dp[i] + 1)
            count += dp[i - 1]

        return count


solution = Solution()
print(solution.candy(ratings=[1, 0, 2]))
