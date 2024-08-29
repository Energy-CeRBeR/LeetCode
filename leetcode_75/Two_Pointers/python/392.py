class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 > l2:
            return False

        if l1 == 0:
            return True

        j = 0
        for i in range(l2):
            if t[i] == s[j]:
                j += 1
            if j == l1:
                return True

        return False


solution = Solution()
print(solution.isSubsequence(s="abc", t="ahbgdc"))
