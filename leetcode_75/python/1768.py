class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l1 = len(word1)
        l2 = len(word2)
        ptr1 = ptr2 = 0
        while ptr1 < l1 or ptr2 < l2:
            if ptr1 < l1:
                result += word1[ptr1]
                ptr1 += 1
            if ptr2 < l2:
                result += word2[ptr2]
                ptr2 += 1
        return result