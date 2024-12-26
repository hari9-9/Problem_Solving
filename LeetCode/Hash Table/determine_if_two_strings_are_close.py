class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1 = {}
        h2 = {}
        if len(word1) != len(word2):
            return False
        for w in word1:
            h1[w] = h1.get(w,0)+1
        for w in word2:
            h2[w] = h2.get(w,0)+1
        sorted_1 = sorted(h1.values())
        sorted_2 = sorted(h2.values())
        return sorted_1 == sorted_2 and set(h1.keys())== set(h2.keys())
        
