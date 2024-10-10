from collections import defaultdict
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(sorted(strs))
        d = defaultdict(int)
        n = len(strs)

        for word in strs:
            pref = ""
            for c in word:
                pref += c
                d[pref] += 1

        ans = ""
        for word, count in d.items():
            if count == n:
                ans = max(ans, word, key=len)

        return ans


solution = Solution()
print(solution.longestCommonPrefix(strs = ["flower","flow","flight"]))
