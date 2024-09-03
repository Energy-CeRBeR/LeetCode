from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)

        d1 = a.difference(b)
        d2 = b.difference(a)

        return [list(d1), list(d2)]
