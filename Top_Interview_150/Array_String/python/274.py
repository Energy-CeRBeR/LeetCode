from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        j = 0
        h = -1
        for i in range(1000):
            while j < n and citations[j] < i:
                j += 1

            if n - j >= i:
                h = i

        return h


solution = Solution()
print(solution.hIndex(citations = [3,0,6,1,5]))
