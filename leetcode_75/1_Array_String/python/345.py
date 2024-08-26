class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        ptr1 = 0
        ptr2 = len(s) - 1
        list_s = list(s)
        while ptr1 <= ptr2:
            flag = True
            while s[ptr1] not in vowels or s[ptr2] not in vowels:
                if s[ptr1] not in vowels:
                    ptr1 += 1
                if s[ptr2] not in vowels:
                    ptr2 -= 1
                if ptr1 > ptr2:
                    flag = False
                    break
            if flag:
                list_s[ptr1], list_s[ptr2] = list_s[ptr2], list_s[ptr1]
                ptr1 += 1
                ptr2 -= 1

        return "".join(list_s)


solution = Solution()
print(solution.reverseVowels("leetcode"))
