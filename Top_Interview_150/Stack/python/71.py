class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [path[0]]

        ptr = 1
        while ptr < len(path):
            cur = path[ptr]
            if cur != "/":
                stack.append(cur)
            else:
                if len(stack) > 2 and stack[-1] == "." and stack[-2] == "." and stack[-3] == "/":
                    count = 0
                    while stack and count < 2:
                        if stack[-1] == "/":
                            count += 1
                        stack.pop()
                    stack.append("/")

                elif len(stack) > 1 and stack[-1] == "." and stack[-2] == "/":
                    stack.pop()

                if stack[-1] != "/":
                    stack.append(cur)

            ptr += 1

        if len(stack) > 1 and stack[-1] == "." and stack[-2] == "/":
            stack.pop()

        elif len(stack) > 2 and stack[-1] == "." and stack[-2] == "." and stack[-3] == "/":
            count = 0
            while stack and count < 2:
                if stack[-1] == "/":
                    count += 1
                stack.pop()
            stack.append("/")

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack)
