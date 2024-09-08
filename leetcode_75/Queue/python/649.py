from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue_R = deque()
        queue_D = deque()
        for i in range(n):
            if senate[i] == "R":
                queue_R.append(i)
            else:
                queue_D.append(i)

        while queue_R and queue_D:
            r_index = queue_R.popleft()
            d_index = queue_D.popleft()
            if r_index < d_index:
                queue_R.append(r_index + n)
            else:
                queue_D.append(d_index + n)

        return "Radiant" if queue_R else "Dire"


solution = Solution()
print(solution.predictPartyVictory(senate="RD"))
