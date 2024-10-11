class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = {}
        for i in arr:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        s2 = set(s.values())
        return len(s2) == len(s.values())
        
