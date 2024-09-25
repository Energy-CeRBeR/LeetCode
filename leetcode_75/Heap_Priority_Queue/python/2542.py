import heapq

from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        new_lst = list((nums1[i], nums2[i]) for i in range(n))
        new_lst.sort(key=lambda x: -x[1])

        min_heap = []
        s = 0
        result = 0

        for n1, n2 in new_lst:
            s += n1
            heapq.heappush(min_heap, n1)

            if len(min_heap) > k:
                s -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                result = max(result, s * n2)

        return result
