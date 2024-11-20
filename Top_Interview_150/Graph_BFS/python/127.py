from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_wordList = set(wordList)
        if endWord not in set_wordList:
            return 0

        __CASE = 'abcdefghijklmnopqrstuvwxyz'

        words_length = len(beginWord)
        graph = defaultdict(set)
        for word in ([beginWord] + wordList):
            if word not in graph:
                graph[word] = set()
            for i in range(words_length):
                for c in __CASE:
                    new_word = word[:i] + c + word[i + 1:]
                    if word != new_word and new_word in set_wordList:
                        graph[word].add(new_word)
                        graph[new_word].add(word)

        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            cur_word, length = queue.popleft()

            if cur_word == endWord:
                return length

            if cur_word in visited:
                continue

            visited.add(cur_word)

            for new_word in graph[cur_word]:
                if new_word not in visited:
                    queue.append((new_word, length + 1))

        return 0
