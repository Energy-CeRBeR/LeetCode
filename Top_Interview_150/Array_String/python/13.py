class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        special_numbers = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        n = len(s)
        i = 0
        int_result = 0
        while i < n:
            if (i + 1) < n and s[i] + s[i + 1] in special_numbers:
                int_result += special_numbers[s[i] + s[i + 1]]
                i += 2
            else:
                int_result += roman_values[s[i]]
                i += 1

        return int_result
