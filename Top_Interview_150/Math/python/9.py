class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x != 0 and x % 10 == 0:
            return False

        reversed_x = 0
        t = x
        while t > 0:
            reversed_x *= 10
            reversed_x += t % 10
            t //= 10

        return x == reversed_x


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         str_x = str(x)
#         return str_x == str_x[::-1]
