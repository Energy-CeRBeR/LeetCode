from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = [1] * n
        p2 = [1] * n

        for i in range(1, n):
            p1[i] = p1[i - 1] * nums[i - 1]
            p2[i] = p2[i - 1] * nums[n - i]

        result = [0] * n
        for i in range(n):
            result[i] = p1[i] * p2[n - i - 1]

        return result


solution = Solution()
print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
