class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = []
        ans.append(intervals[0])

        for start , stop in intervals[1:]:
            if start > ans[-1][1]:
                ans.append([start,stop])
            else:
                ans[-1][1] = max(stop , ans[-1][1])
        return ans
