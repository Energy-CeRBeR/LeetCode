from typing import List, Tuple


class Solution:

    @staticmethod
    def greedy_fill(words: List[str], maxWidth: int) -> List[Tuple]:
        n = len(words)

        result = []
        cur_data = [words[0]]
        cur_size = len(words[0])
        for i in range(1, n):
            word = words[i]
            if cur_size + 1 + len(word) <= maxWidth:
                cur_data.append(word)
                cur_size += 1 + len(word)
            else:
                result.append(
                    (cur_data, maxWidth - (cur_size - len(cur_data) + 1)))
                cur_data = [word]
                cur_size = len(word)

        if cur_size:
            result.append(
                (cur_data, maxWidth - (cur_size - len(cur_data) + 1)))

        return result

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        strings = self.greedy_fill(words, maxWidth)

        response = []
        for i in range(len(strings) - 1):
            data, count = strings[i]
            cur_string = data[0]

            space_places = len(data) - 1
            if space_places == 0:
                cur_string += count * " "
                response.append(cur_string)
                continue

            count_spaces = count // space_places
            ost_spaces = count - (count_spaces * space_places)

            for i in range(1, len(data)):
                cur_string += " " * count_spaces
                if ost_spaces:
                    cur_string += " "
                    ost_spaces -= 1
                cur_string += data[i]

            response.append(cur_string)

        data, count = strings[-1]
        response.append(" ".join(data) + " " * (count - len(data) + 1))

        return response


solution = Solution()
print(solution.fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough", "to",
      "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
