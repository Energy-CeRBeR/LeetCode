from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = dict()
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for num in counter.keys():
            if counter[num] == 1:
                return num
