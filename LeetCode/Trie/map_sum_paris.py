class TrieNode:
    def __init__(self):
        self.children = [None] *26
        self.value = 0
    def insert(self , word: str, val: int):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.value += val

    def search(self , word: str):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return 0
            node = node.children[index]
        return node.value


class MapSum:

    def __init__(self):
        self.dictionary = defaultdict(int)
        self.trie_root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dictionary[key]
        self.dictionary[key] = val
        self.trie_root.insert(key,delta)


    def sum(self, prefix: str) -> int:
        return self.trie_root.search(prefix)



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
