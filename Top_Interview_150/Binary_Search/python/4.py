from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                merged_nums.append(nums1[ptr1])
                ptr1 += 1
            else:
                merged_nums.append(nums2[ptr2])
                ptr2 += 1

        while ptr1 < len(nums1):
            merged_nums.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < len(nums2):
            merged_nums.append(nums2[ptr2])
            ptr2 += 1

        if len(merged_nums) % 2 != 0:
            return merged_nums[len(merged_nums) // 2]
        else:
            return (merged_nums[len(merged_nums) // 2 - 1] + merged_nums[len(merged_nums) // 2]) / 2


solution = Solution()
print(solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
