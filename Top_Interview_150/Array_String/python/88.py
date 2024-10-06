from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

#         nums1_count = ptr1 = ptr2 = 0
#         while nums1_count < m and ptr2 < n:
#             if nums1[ptr1] > nums2[ptr2]:
#                 nums1.insert(ptr1, nums2[ptr2])
#                 nums1.pop()
#                 ptr2 += 1
#             else:
#                 nums1_count += 1

#             ptr1 += 1

#         while ptr2 < n:
#             nums1[ptr1] = nums2[ptr2]
#             ptr1 += 1
#             ptr2 += 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
