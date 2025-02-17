class MagicDictionary:

    def __init__(self):
        self.hash = {}
        self.exc = set()


    def buildDict(self, dictionary: List[str]) -> None:
        self.exc = set(dictionary)
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                self.hash[pattern] = self.hash.get(pattern,0)+1

    def search(self, searchWord: str) -> bool:

        for i in range(len(searchWord)):
            pattern = searchWord[:i]+ "*" + searchWord[i+1:]
            count = self.hash.get(pattern,0)
            if count > 1 or (count ==1 and searchWord not in self.exc):
                return True
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
