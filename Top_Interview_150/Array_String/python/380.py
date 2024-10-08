from random import choice


class RandomizedSet:

    def __init__(self):
        self.hash_lst = dict()
        self.lst = list()

    def insert(self, val: int) -> bool:
        if val not in self.hash_lst:
            self.lst.append(val)
            self.hash_lst[val] = len(self.st) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_lst:
            idx = self.hash_lst[val]
            self.lst[idx] = self.lst[-1]
            self.hash_lst[self.lst[-1]] = idx
            self.lst.pop()

            del self.hash_lst[val]
            return True

        return False

    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
