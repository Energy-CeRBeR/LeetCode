from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        counter_index = 1
        start_index = 0
        for i in range(1, len(chars)):
            if chars[i] != chars[start_index]:
                if counter > 1:
                    for c in str(counter):
                        chars[counter_index] = c
                        counter_index += 1
                start_index = i
                counter = 1
                counter_index = i + 1
            else:
                chars[i] = ""
                counter += 1

        if not chars[-1]:
            for c in str(counter):
                chars[counter_index] = c
                counter_index += 1

        ind = 0
        while ind < len(chars):
            if not chars[ind]:
                del chars[ind]
                ind -= 1
            ind += 1
            
        print(chars)
        return len(chars)


solution = Solution()
print(solution.compress(["a", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b", "b"]))
