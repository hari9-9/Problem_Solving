"""
this is my original solution
Runtime: 116 ms
Memory Usage: 15.1 MB
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s)) <= 1: return True
        
        s = s.lower()
        t = []
        i=0
        while(i<len(s)):
            if s[i].isalpha() or s[i].isdigit():
                t.append(s[i])
            i+=1

        l = len(t)
        s="".join(t)
        for i in range(int(l/2)):
            t[i], t[l-i-1] = t[l-i-1], t[i]
        t = "".join(t)
        s = "".join(s)
        return (t==s)
