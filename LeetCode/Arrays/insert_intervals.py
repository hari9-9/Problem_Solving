class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        ans=[]
        ans.append(intervals[0])
        for start , end in intervals[1:]:
            if start > ans[-1][1]:
                ans.append([start,end])
            else:
                ans[-1][1] = max(ans[-1][1],end)
        return ans
