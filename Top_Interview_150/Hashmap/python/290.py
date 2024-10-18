class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = dict()
        words = s.split()

        if len(pattern) != len(words):
            return False

        added_words = set()
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if words[i] not in added_words:
                    dct[pattern[i]] = words[i]
                    added_words.add(words[i])
                else:
                    return False

            else:
                if words[i] != dct[pattern[i]]:
                    return False

        return True
