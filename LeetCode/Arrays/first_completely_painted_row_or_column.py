class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hash = {}
        rows , cols = len(mat) , len(mat[0])
        for i in range(rows):
            for j in range(cols):
                hash[mat[i][j]] = (i,j)

        numr = [0]*rows
        numc = [0]*cols
        for i in range(len(arr)):
            r ,c  = hash[arr[i]]
            numr[r] += 1
            numc[c] += 1
            if numr[r] == cols or numc[c] == rows:
                return i
        return -1
