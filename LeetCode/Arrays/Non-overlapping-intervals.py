class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        print(intervals)
        ans = []
        ans.append(intervals[0])
        n=0
        for start , end in intervals[1:]:
            if start < ans[-1][1]:
                ans[-1][1] = min(ans[-1][1] , end)
                n+=1
            else:
                ans.append([start,end])
        return n
        
