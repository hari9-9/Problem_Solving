class Solution:

    class TrieNode:
        def __init__(self):
            self.frequency = 0
            self.child = {}

    def _insert_word(self,root,word):
        curr = root
        for c in word:
            if c not in curr.child:
                curr.child[c] = self.TrieNode()
            curr = curr.child[c]
            curr.frequency +=1
    
    def _is_sub(self,root,word):
        curr = root
        for c in word:
            curr = curr.child[c]
        return curr.frequency > 1


    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        root = self.TrieNode()
        for word in words:
            for i in range(len(word)):
                self._insert_word(root, word[i:])
        
        for word in words:
            if self._is_sub(root,word):
                ans.append(word)
        
        return ans
        
