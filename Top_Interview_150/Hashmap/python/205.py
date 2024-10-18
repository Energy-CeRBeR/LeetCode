class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if not sorted(s.count(c) for c in set(s)) == sorted(t.count(c) for c in set(t)):
            return False

        n = len(s)
        dct = {c: c for c in set(s)}

        for i in range(n):
            if s[i] != t[i]:
                dct[s[i]] = t[i]

        new_s = "".join(dct[c] for c in s)
        print(new_s)

        return new_s == t


solution = Solution()
print(solution.isIsomorphic(s="badc", t="baba"))
