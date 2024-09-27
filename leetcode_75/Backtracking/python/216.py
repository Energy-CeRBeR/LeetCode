from typing import List


# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:

#         def backtracking(cur_data, cur_num, target, result):
#             target -= cur_num
#             if target == 0 and len(cur_data) == k:
#                 cur_data = sorted(cur_data)
#                 if cur_data not in result:
#                     result.append(cur_data)

#             if target > 0 and len(cur_data) < k:
#                 for i in range(1, 10):
#                     if i not in cur_data:
#                         backtracking(cur_data + [i], i, target, result)

#             return result

#         return backtracking([], 0, n, [])


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(start, path, target):
            if len(path) == k and target == 0:
                result.append(path[:])
                return

            if len(path) >= k or target < 0:
                return

            for i in range(start, 10):
                path.append(i)
                backtracking(i + 1, path, target - i)
                path.pop()

        result = []
        backtracking(1, [], n)
        return result
