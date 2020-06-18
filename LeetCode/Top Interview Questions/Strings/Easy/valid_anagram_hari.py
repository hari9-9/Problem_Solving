class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        print(cs,ct)
        
        for c in ct:
            print(c,ct[c])
            print(c,cs[c])
            if(not (ct[c]<=cs[c])):
                return False
        return True
