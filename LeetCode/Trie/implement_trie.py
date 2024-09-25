class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

    def __str__(self):
        return str(self.val)


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode(l)
                cur = cur.children[l]
            else:
                cur = cur.children[l]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            if l in cur.children:
                cur = cur.children[l]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)