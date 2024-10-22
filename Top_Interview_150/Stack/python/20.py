class Solution:

    __parenthesis_1 = {"(": ")", "{": "}", "[": "]"}
    __parenthesis_2 = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        if s[0] in self.__parenthesis_2:
            return False

        stack = [s[0]]
        ptr = 1
        while ptr < len(s):
            if s[ptr] in self.__parenthesis_1:
                stack.append(s[ptr])
            else:
                if stack and stack[-1] == self.__parenthesis_2[s[ptr]]:
                    stack.pop()
                else:
                    return False
                
            ptr += 1

        return len(stack) == 0


solution = Solution()
print(solution.isValid(s="([])"))
