class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        n = len(s)
        result = [""] * numRows

        j = 0
        d = 1
        for i in range(n):
            result[j] += s[i]

            if j == 0:
                d = 1
            elif j == numRows - 1:
                d = -1
            j += d

        return "".join(result)


solution = Solution()
print(solution.convert(s="AB", numRows=1))
