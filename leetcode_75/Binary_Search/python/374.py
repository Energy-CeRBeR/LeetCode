# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


def guess(num: int,) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        num = (left + right) // 2

        response = guess(num)
        while response != 0:
            if response == -1:
                right = num - 1
                num = (left + right) // 2
            else:
                left = num + 1
                num = (left + right) // 2
            response = guess(num)

        return num
