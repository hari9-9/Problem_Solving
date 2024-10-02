class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = arr.copy()
        copy.sort()
        hmap = {}
        rank =1
        for i in copy:
            if i not in hmap:
                hmap[i] = rank
                rank+=1
        ans = []
        for i in arr:
            ans.append(hmap[i])
        return ans
