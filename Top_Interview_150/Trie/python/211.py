class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = dict()
            cur_node = cur_node[c]
        cur_node["+"] = ""

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return "+" in node

            if word[index] == ".":
                for new_node in node:
                    if new_node != "+":
                        if dfs(node[new_node], index + 1):
                            return True
                return False

            if word[index] in node:
                return dfs(node[word[index]], index + 1)

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
