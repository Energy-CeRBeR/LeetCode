from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ind = 0
        two_last_zeros_indexes = []
        size = len(nums)
        while ind < size:
            if nums[ind] == 0:
                two_last_zeros_indexes.append(ind)
                if len(two_last_zeros_indexes) == 2:
                    break
            ind += 1

        if len(two_last_zeros_indexes) < 2:
            return size - 1

        mx = ind - 1
        start_pos = two_last_zeros_indexes[0] + 1
        for i in range(ind + 1, size):
            if nums[i] == 0:
                mx = max(mx, i - start_pos - 1)
                two_last_zeros_indexes[0] = two_last_zeros_indexes[1]
                two_last_zeros_indexes[1] = i
                start_pos = two_last_zeros_indexes[0] + 1
            else:
                mx = max(mx, i - start_pos)

        return mx
