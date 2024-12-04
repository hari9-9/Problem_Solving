from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Array for 26 lowercase letters
        self.value = 0  # Value stored at this node

    def insert(self, word: str, val: int):
        print(f"Inserting '{word}' with value delta {val}")
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
                print(f"  Creating new TrieNode for '{char}'")
            else:
                print(f"  Moving to existing TrieNode for '{char}'")
            node = node.children[index]
            node.value += val
            print(f"  Node value at '{char}' updated to {node.value}")

    def search(self, word: str):
        print(f"Searching for prefix '{word}'")
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                print(f"  Prefix '{word}' not found, returning 0")
                return 0
            print(f"  Moving to TrieNode for '{char}' with value {node.children[index].value}")
            node = node.children[index]
        print(f"Total sum for prefix '{word}' is {node.value}")
        return node.value


class MapSum:
    def __init__(self):
        self.dictionary = defaultdict(int)  # Store the latest values for keys
        self.trie_root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        print(f"Inserting key-value pair ('{key}', {val})")
        delta = val - self.dictionary[key]  # Calculate the change in value
        print(f"Value delta for key '{key}' is {delta}")
        self.dictionary[key] = val
        self.trie_root.insert(key, delta)

    def sum(self, prefix: str) -> int:
        print(f"Calculating sum for prefix '{prefix}'")
        result = self.trie_root.search(prefix)
        print(f"Sum for prefix '{prefix}' is {result}")
        return result
