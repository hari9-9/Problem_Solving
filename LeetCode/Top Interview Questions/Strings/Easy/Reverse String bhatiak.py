"""
this is my original solution.
Runtime: 220 ms
Memory Usage: 18.1 MB
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=len(s)
        for i in range(int(l/2)):
            s[i], s[l-i-1] = s[l-i-1], s[i]
