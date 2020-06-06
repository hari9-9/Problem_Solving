"""
this is my original solution.
time: 120 ms
space: 20.2 MB
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i in nums:
            if i in dups:
                return True
            else:
                dups[i] = 0
        return False
