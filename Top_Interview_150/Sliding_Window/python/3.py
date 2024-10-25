class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        start = 0
        mx = 0
        for i in range(len(s)):
            if s[i] in hash_table and hash_table[s[i]] >= start:
                start = hash_table[s[i]] + 1
            hash_table[s[i]] = i
            mx = max(mx, i - start + 1)

        return mx
