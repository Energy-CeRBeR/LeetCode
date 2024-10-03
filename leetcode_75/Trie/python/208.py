class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = dict()
            cur_node = cur_node[c]

        cur_node["+"] = ""

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]

        return "+" in cur_node

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
