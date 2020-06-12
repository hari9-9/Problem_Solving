"""
this is my original solution.
Runtime: 52 ms
Memory Usage: 14 MB
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        ds, dt = {}, {}

        for i in range(len(s)):
            if s[i] in ds:
                ds[s[i]] += 1 
            else:
                ds[s[i]] = 1

            if t[i] in dt:
                dt[t[i]] += 1    
            else:
                dt[t[i]] = 1

        return True if ds==dt else False
