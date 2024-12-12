class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        # Sort by frequency (descending) and then alphabetically (ascending)
        sorted_words = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))
        return sorted_words[:k]
