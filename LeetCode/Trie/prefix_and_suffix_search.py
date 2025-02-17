class TrieNode:
    def __init__(self):
        self.child = {}
        self.indices = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word,i):
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
            curr.indices.append(i)

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.child:
                return []
            curr = curr.child[char]
        return curr.indices



class WordFilter:

    def __init__(self, words: List[str]):
        self.preTrie = Trie()
        self.sufTrie = Trie()
        for index ,word in enumerate(words):
            self.preTrie.insert(word,index)
            self.sufTrie.insert(word[::-1],index)


    def f(self, pref: str, suff: str) -> int:
        pre = self.preTrie.search(pref)
        suf = self.sufTrie.search(suff[::-1])
        p1 = len(pre)-1
        p2 = len(suf)-1
        while p1 >=0 and p2>=0:
            if pre[p1] == suf[p2]:
                return pre[p1]
            elif pre[p1] > suf[p2]:
                p1-=1
            else:
                p2-=1
        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
