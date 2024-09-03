from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        size = len(arr)
        d = dict()
        for i in range(size):
            if arr[i] not in d:
                d[arr[i]] = 0
            d[arr[i]] += 1

        values = d.values()
        if len(set(values)) != len(values):
            return False
        return True


solution = Solution()
print(solution.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
