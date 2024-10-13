class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        n = len(s)
        ptr_s = 0
        for c in t:
            if c == s[ptr_s]:
                ptr_s += 1

            if ptr_s == n:
                return True

        return False
