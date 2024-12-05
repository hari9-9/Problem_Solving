class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            c_index = ord(c) - ord('a')
            if node.child[c_index] is None:
                node.child[c_index] = TrieNode()
            node = node.child[c_index]
        node.end = True


    def search(self, word: str) -> bool:
        def dfs(index,node):
            for i in range(index,len(word)):
                char = word[i]
                c_index = ord(char) - ord('a')
                if char == '.':
                    for child in node.child:
                        if child is not None and dfs(i+1,child):
                            return True
                    return False
                elif node.child[c_index] is None:
                    return False
                node = node.child[c_index]
            return node.end
        return dfs(0,self.root)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
