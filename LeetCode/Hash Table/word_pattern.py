class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i =-1
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        print(words)
        hash = {}
        for w in words:
            i+=1
            curr = pattern[i]
            print("curr"+curr)
            if curr in hash:
                if hash[curr] == w:
                    continue
                else:
                    return False
            else:
                if w not in hash.values():
                    hash[curr]=w
                else:
                    return False
        return True
        
