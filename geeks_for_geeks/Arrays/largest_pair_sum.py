from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        m1 = -1
        m2 = -1
        for i in arr:
            if i >m1:
                m2 = m1
                m1 = i
            elif i>m2 and i<m1:
                m2 = i
        return m1+m2
