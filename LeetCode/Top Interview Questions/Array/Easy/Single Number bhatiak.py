"""
this is my original solution.
time: 84 ms
space: 16.4 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dups = {}
        for i in nums:
            if i in dups:
                del dups[i]
            else:
                dups[i] = 0
        return list(dups)[0]
