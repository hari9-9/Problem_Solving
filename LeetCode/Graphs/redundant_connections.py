class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [i for i in range(len(edges)+1)]
        r = [1] * (len(edges)+1)

        def find(n):
            res = p[n]
            while res != p[res]:
                p[res] = p[p[res]]
                res = p[res]
            return res

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return False

            if r[p1] > r[p2]:
                p[p2] = p1
                r[p1]+=r[p2]
            else:
                p[p1] = p2
                r[p2]+=r[p1]
            return True
        for n1 ,n2 in edges:
            ans = union(n1,n2)
            if not ans:
                return [n1,n2]
