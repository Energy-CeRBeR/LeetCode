from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeros_indexes = list()
        prev_zero = 0
        zeros_counter = 0

        ind = 0
        while ind < len(nums):
            if nums[ind] == 0:
                zeros_indexes.append(ind)
                zeros_counter += 1
                if zeros_counter > k:
                    break
            ind += 1

        mx = ind
        zeros_counter -= 1

        for i in range(ind + 1, len(nums)):
            if nums[i] != 0:
                mx = max(mx, i - zeros_indexes[prev_zero])
            else:
                zeros_indexes.append(i)
                zeros_counter += 1
                mx = max(mx, i - zeros_indexes[prev_zero] - 1)
                prev_zero += 1
                zeros_counter -= 1

        return mx
