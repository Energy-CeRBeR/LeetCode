from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref1 = [1]
        pref2 = [1]
        for i in range(n):
            pref1.append(pref1[i] * nums[i])
            pref2.append(pref2[i] * nums[n - i - 1])
        pref2.reverse()

        result = list()
        for i in range(n):
            result.append(pref1[i] * pref2[i + 1])

        return result
