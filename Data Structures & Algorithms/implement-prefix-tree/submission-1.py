#0: Non existent
#1: Prefix
#2: Word
#3: Both

class PrefixTree:

    def __init__(self):
        self.mp = defaultdict(int)

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if self.mp[word[:i]] in (2,3):
                self.mp[word[:i]] = 3
            else:
                self.mp[word[:i]] = 1
        if self.mp[word] in (1,3):
            self.mp[word] = 3
        else:
            self.mp[word] = 2

    def search(self, word: str) -> bool:
        return self.mp[word] in (2,3)
        

    def startsWith(self, prefix: str) -> bool:
        return self.mp[prefix] != 0
        
        