from typing import List
import heapq


# class Solution:
#     def findKthLargest(self, nums, k):
#         return sorted(nums, reverse=True)[k - 1]


# class Solution:

#     class MaxHeap:
#         def __init__(self) -> None:
#             self.heap = [0]
#             self.size = 0

#         def shiftUP(self, i):
#             while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
#                 self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
#                 i //= 2

#         def insert(self, x):
#             self.heap.append(x)
#             self.size += 1
#             self.shiftUP(self.size)

#         def shiftDown(self, i):
#             while i * 2 <= self.size:
#                 j = self.maxChild(i)
#                 if self.heap[i] < self.heap[j]:
#                     self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#                 i = j

#         def maxChild(self, i):
#             if i * 2 + 1 > self.size:
#                 return i * 2
#             if self.heap[i * 2] > self.heap[i * 2 + 1]:
#                 return i * 2
#             return i * 2 + 1

#         def get_max(self):
#             if self.size == 0:
#                 return None
#             return self.heap[1]

#         def pop_max(self):
#             response = self.heap[1]
#             self.heap[1] = self.heap[self.size]
#             self.heap.pop()
#             self.size -= 1
#             self.shiftDown(1)

#             return response

#         def __str__(self):
#             return str(self.heap)

#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = self.MaxHeap()
#         for item in nums:
#             heap.insert(item)

#         data = None
#         while k != 0:
#             data = heap.pop_max()
#             k -= 1

#         return data


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for item in nums:
            heapq.heappush(heap, -item)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
