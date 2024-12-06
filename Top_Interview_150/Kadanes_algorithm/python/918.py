from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        currMin = 0
        maxSum = nums[0]
        currSum = 0
        total = 0

        for num in nums:
            currSum = max(currSum, 0)
            currSum += num

            maxSum = max(currSum, maxSum)
            currMin = min(currMin, 0)

            currMin += num
            minSum = min(minSum, currMin)
            total += num

        if maxSum < 0:
            return maxSum
        
        return max(total - minSum, maxSum)
