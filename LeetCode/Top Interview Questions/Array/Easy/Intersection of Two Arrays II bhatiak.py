"""
this is my original solution
time: 48 ms
space: 13.7 MB
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        d = {}

        for i in nums1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            d[(i, count[i])] = 1

        count = {}
        for i in nums2:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if (i, count[i]) in d:
                d[(i, count[i])] += 1

        vals = []
        for key in d:
            if d[key] > 1:
                vals.append(key[0])

        return vals
