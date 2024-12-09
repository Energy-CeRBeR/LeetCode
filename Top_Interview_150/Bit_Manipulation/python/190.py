class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = bin(n)[2:][::-1]
        while len(reversed_num) < 32:
            reversed_num = reversed_num + "0"

        return int(reversed_num, 2)
