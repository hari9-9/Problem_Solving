class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        h1 = {}
        h2 = {}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count +=1
            if count >2:
                return False
            h1[s1[i]] = h1.get(s1[i],0)+1
            h2[s2[i]] = h2.get(s2[i],0)+1

        return h1 == h2
        
