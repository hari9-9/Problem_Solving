class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        change = 0
        count = 0
        for c in s:
            if c == curr:
                count+=1
                continue
            if count%2 == 0:
                count =1
            else:
                count = 0
                change+=1
            curr = c
        return change
        
