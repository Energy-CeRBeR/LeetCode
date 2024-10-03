from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            if len(node.words) < 3:
                node.words.append(word)

    def find_word_by_prefix(self, c):
        if self.node and c in self.node.children:
            self.node = self.node.children[c]
            return self.node.words
        else:
            self.node = None
            return []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()

        for product in products:
            trie.insert(product)

        return [trie.find_word_by_prefix(c) for c in searchWord]
