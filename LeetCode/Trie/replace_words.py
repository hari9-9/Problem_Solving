class Trie:
    def __init__(self):
        self.child = [None] *26
        self.ref = -1
    def insert(self, word , index):
        node = self
        for char in word:
            char_index = ord(char)-ord('a')
            if node.child[char_index] is None:
                node.child[char_index] = Trie()
            node = node.child[char_index]
        node.ref = index
    def search(self, word):
        node = self
        for char in word:
            char_index = ord(char) - ord('a')
            if node.child[char_index] == None:
                return -1
            node = node.child[char_index]
            if node.ref != -1:
                return node.ref
        return -1


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for inx , word in enumerate(dictionary):
            trie.insert(word,inx)

        ans = []
        for word in sentence.split():
            index = trie.search(word)
            ans.append(dictionary[index] if index !=-1 else word)
        return " ".join(ans)
