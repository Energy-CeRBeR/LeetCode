from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)

        left = 0
        right = length - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[-1]:
                left = middle + 1
            else:
                right = middle - 1

        pivot = left
        left = 0
        right = length - 1
        while left <= right:
            middle = (left + right) // 2
            real_middle = (middle + pivot) % length
            if nums[real_middle] == target:
                return real_middle
            elif nums[real_middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] >= nums[left]:
#                 if nums[left] <= target <= nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] <= target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return -1
