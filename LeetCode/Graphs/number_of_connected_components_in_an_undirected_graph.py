from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        p = [i for i in range(n)]
        r = [1]*n

        def find(n1):
            res = n1
            while p[res] != res:
                p[res] = p[p[res]]
                res = p[res]
            return res

        def unios(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return 0
            if r[p2] > r[p1]:
                p[p1] = p2
                r[p2] +=r[p1]
            else:
                p[p2] = p1
                r[p1] +=r[p2]
            return 1

        res = n
        for n1,n2 in edges:
            res-=unios(n1,n2)
        return res
