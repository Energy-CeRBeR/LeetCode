class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNote_case = {c: ransomNote.count(c) for c in ransomNote}
        for c in magazine:
            if c in ransomNote_case:
                ransomNote_case[c] -= 1

        print(ransomNote_case)

        return all(c <= 0 for c in ransomNote_case.values())


solution = Solution()
print(solution.canConstruct(ransomNote="aa", magazine="ab"))
