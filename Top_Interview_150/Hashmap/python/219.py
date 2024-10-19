from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = dict()
        for i in range(len(nums)):
            if nums[i] in dct:
                if i - dct[nums[i]] <= k:
                    return True
            dct[nums[i]] = i

        return False
