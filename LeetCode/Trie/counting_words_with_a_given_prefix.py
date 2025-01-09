class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class Solution:
    def insertWord(self,root, word):
        curr = root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.count +=1

    def getFreq(self , root, word):
        curr = root
        for c in word:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.count

    def prefixCount(self, words: List[str], pref: str) -> int:
        root = TrieNode()

        for word in words:
            self.insertWord(root,word[:len(pref)])

        ans = self.getFreq(root,pref)
        return ans
