class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        mx = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            mx = max(mx, count)

        return mx
