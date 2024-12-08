import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []
        
        for num in nums1:
            heapq.heappush(heap, (num + nums2[0], 0))
        
        while k > 0 and heap:
            nums_sum, index = heapq.heappop(heap)
            result.append([nums_sum - nums2[index], nums2[index]])
            
            if index + 1 < len(nums2):
                heapq.heappush(heap, (nums_sum - nums2[index] + nums2[index + 1], index + 1))
            
            k -= 1
        
        return result
