from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [0] * (n + 2)
        dp[1] = cost[0]

        for i in range(2, n + 2):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]

        return dp[-1]
