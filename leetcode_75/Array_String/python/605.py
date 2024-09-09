from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            counter += 1

        if len(flowerbed) >= 2:
            if not flowerbed[0] and not flowerbed[1]:
                flowerbed[0] = 1
                counter += 1
        for i in range(2, len(flowerbed)):
            if all(not x for x in flowerbed[i - 2: i + 1]):
                flowerbed[i - 1] = 1
                counter += 1
            if counter == n:
                break

        if len(flowerbed) >= 2 and not flowerbed[-2] and not flowerbed[-1]:
            counter += 1

        if counter >= n:
            return True
        return False


solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], n=2))
