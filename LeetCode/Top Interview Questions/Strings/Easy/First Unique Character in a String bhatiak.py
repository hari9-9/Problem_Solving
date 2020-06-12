"""
this is my original solution.
Runtime: 220 ms
Memory Usage: 13.9 MB
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = [d[s[i]][0], d[s[i]][1] + 1]    
            else:
                d[s[i]] = [i, 1]

        for letter in d:
            if d[letter][1] == 1:
                return d[letter][0]
        return -1
