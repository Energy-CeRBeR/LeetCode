class Solution:

    __case = set('abcdefghijklmnopqrstuvwxyz0123456789')

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:

            a = s[left].lower()
            b = s[right].lower()

            if a in self.__case and b in self.__case:
                if a != b:
                    return False

                left += 1
                right -= 1

            elif a not in self.__case and b not in self.__case:
                left += 1
                right -= 1

            elif a not in self.__case:
                left += 1

            elif b not in self.__case:
                right -= 1

        return True
