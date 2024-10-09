from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        station = 0
        s = 0
        n = len(gas)

        while station - start < n:
            s += gas[station] - cost[station]
            while station - start < n and s < 0:
                start -= 1
                s += gas[start] - cost[start]
            station += 1

        if s >= 0:
            return start if start >= 0 else n + start
        return -1
