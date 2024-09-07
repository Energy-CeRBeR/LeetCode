from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        digit_stack = deque()
        letter_stack = deque()
        ans = ""
        last_symbol = ""
        for c in s:
            if c.isdigit():
                if not last_symbol.isdigit():
                    digit_stack.append(c)
                else:
                    digit_stack[-1] += c

            elif c == "[":
                letter_stack.append("")

            elif c.isalpha():
                if len(letter_stack) > 0:
                    letter_stack[-1] += c
                else:
                    ans += c

            elif c == "]":
                digit = int(digit_stack.pop())
                letter = letter_stack.pop()
                if len(letter_stack) > 0:
                    letter_stack[-1] += letter * digit
                else:
                    ans += letter * digit

            last_symbol = c

        return ans


solution = Solution()
print(solution.decodeString("100[leetcode]"))
