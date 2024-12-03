from typing import List

class TrieNode:
    def __init__(self, val='', is_end=False):
        self.val = val
        self.child = [None] * 26
        self.child_count = 0
        self.is_end = is_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char: str) -> int:
        """Convert a character to its corresponding index (0-25)."""
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = self._char_to_index(c)
            if curr.child[index] is None:
                curr.child[index] = TrieNode(c)
                curr.child_count += 1
            curr = curr.child[index]
        curr.is_end = True

    def longest_prefix(self) -> str:
        curr = self.root
        ans = []
        while curr and curr.child_count == 1 and not curr.is_end:
            # Find the single child
            for i in range(26):
                if curr.child[i]:
                    ans.append(chr(i + ord('a')))
                    curr = curr.child[i]
                    break
        return "".join(ans)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        t = Trie()
        for w in strs:
            t.insert(w)
        return t.longest_prefix()
