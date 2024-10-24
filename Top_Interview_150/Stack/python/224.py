from typing import List


class Solution:

    @staticmethod
    def create_postfix(s: str) -> List[str]:
        operations: List[str] = list()
        postfix: List[str] = list()

        priority = {')': -2, '(': -1, '+': 0, '-': 1, '*': 2, '/': 3}

        flag = False
        last_symbol = ""
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                if flag:
                    postfix[-1] += c
                else:
                    postfix.append(c)
                flag = True

            elif c == "(":
                operations.append(c)
                flag = False

            elif c in "+-*/":
                if c == "-" and last_symbol in "(+-*/":
                    postfix.append("0")
                    operations.append(c)

                else:
                    while operations and priority[c] <= priority[operations[-1]]:
                        postfix.append(operations.pop())
                    operations.append(c)
                    flag = False

            elif c == ")":
                while operations[-1] != "(":
                    postfix.append(operations.pop())
                operations.pop()
                flag = False

            else:
                flag = False

            if c != " ":
                last_symbol = c

        while operations:
            postfix.append(operations.pop())

        return postfix

    @staticmethod
    def solve(num1: int, num2: int, operation: str) -> int:
        match operation:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(float(num1) / num2)
            case _:
                return 0

    def calculate(self, s: str) -> int:
        tokens = self.create_postfix(s)

        stack = list()
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(self.solve(x1, x2, token))

        return stack[0]
