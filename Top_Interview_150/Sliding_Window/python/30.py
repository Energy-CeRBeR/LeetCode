from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        word_length = len(words[0])
        for i in range(word_length):
            left = i
            count = 0
            temp_word_count = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in word_count:
                    temp_word_count[word] = temp_word_count.get(word, 0) + 1
                    count += 1

                    while temp_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        temp_word_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == len(words):
                        result.append(left)
                else:
                    temp_word_count.clear()
                    count = 0
                    left = j + word_length

        return result
