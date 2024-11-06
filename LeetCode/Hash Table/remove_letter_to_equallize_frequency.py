class Solution:
    def equalFrequency(self, word: str) -> bool:
        s = list(word)
        #s.sort()
        hash = {}
        for i in s:
            hash[i] = hash.get(i,0)+1
        print(hash)
        for i in hash:
            hash[i]-=1
            print(hash)
            se = set()
            for j in hash:
                if hash.get(j):
                    se.add(hash.get(j))
            if len(se) == 1:
                return True
            hash[i] = hash.get(i,0)+1
        return False        
