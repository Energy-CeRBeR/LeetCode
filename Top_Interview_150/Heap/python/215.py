import heapq


class Solution:
    def findKthLargest(self, nums, k):
        nums = list(map(lambda x: -x, nums))
        
        heapq.heapify(nums)
        num = heapq.heappop(nums)
        for _ in range(k - 1):
            num = heapq.heappop(nums)

        return -num
