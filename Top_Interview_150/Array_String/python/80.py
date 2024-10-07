from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        flag = False
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                flag = False
                nums[index] = nums[i]
                index += 1
            else:
                if not flag:
                    flag = True
                    nums[index] = nums[i]
                    index += 1

        return index
