from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        offset = nums[:n - k]

        count = 0
        i = n - k
        while count < k:
            nums[count] = nums[i]
            count += 1
            i += 1

        for i in range(k, n):
            nums[i] = offset[i - k]

        print(nums)


solution = Solution()
print(solution.rotate(nums=[-1], k=2))
