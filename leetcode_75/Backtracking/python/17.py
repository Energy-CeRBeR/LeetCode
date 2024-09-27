from typing import List


class Solution:

    _CONVERTER = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        def backtracking(combination, digits, result):
            if len(digits) == 0:
                result.append(combination)
            else:
                for c in self._CONVERTER[digits[0]]:
                    backtracking(combination + c, digits[1:], result)
                    
            return result

        return backtracking("", digits, [])
