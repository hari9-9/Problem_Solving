class TrieNode:
    def __init__(self, val , is_end = False):
        self.val = val
        self.child = [None] * 26
        self.is_end = is_end

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def _char_to_index(self, char: str) -> int:
        """Convert a character to its corresponding index (0-25)."""
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = self._char_to_index(c)
            if curr.child[index] is None:
                curr.child[index] = TrieNode(c)
                curr = curr.child[index]
            else:
                curr = curr.child[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = self._char_to_index(c)
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return curr.is_end



    def startsWith(self, prefix: str) -> bool:
        cur = self.root  # Start from the root node
        for l in prefix:  # Loop through each character in the prefix
            index = self._char_to_index(l)  # Convert the character to its corresponding index
            if cur.child[index] is None:  # Check if the child node at this index exists
                return False  # If the node is missing, the prefix is not present
            cur = cur.child[index]  # Move to the next node
        return True  # If all characters are found, return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
