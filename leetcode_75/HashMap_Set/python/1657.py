class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = len(word1)
        l2 = len(word2)
        if l1 != l2:
            return False

        s1 = set(word1)
        s2 = set(word2)
        if s1 != s2:
            return False

        d1 = sorted(word1.count(i) for i in s1)
        d2 = sorted(word2.count(i) for i in s2)

        return d1 == d2
