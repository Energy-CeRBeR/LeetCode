from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('Inf'), float('Inf')
        for ele in nums:
            if ele <= first:
                first = ele
            elif first < ele <= second:
                second = ele
            elif ele > second:
                return True
        return False


solution = Solution()
solution.increasingTriplet(nums=[1, 2, 3, 4, 5])
