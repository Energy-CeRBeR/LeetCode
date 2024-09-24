import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.added_back = set()
        self.next_smallest = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added_back.remove(smallest)
            return smallest

        smallest = self.next_smallest
        self.next_smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.next_smallest and num not in self.added_back:
            heapq.heappush(self.heap, num)
            self.added_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
