class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,w):
        curr = self.root
        for c1 , c2 in zip(w , reversed(w)):
            if (c1,c2) not in curr.child:
                curr.child[(c1,c2)] = TrieNode()
            curr = curr.child[(c1,c2)]
            curr.count+=1

    def count(self , w):
        curr = self.root
        for c1 , c2 in zip(w , reversed(w)):
            if (c1,c2) not in curr.child:
                return 0
            curr = curr.child[(c1,c2)]
        return curr.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        root = Trie()
        for w in reversed(words):
            res+=root.count(w)
            root.add(w)
        return res
