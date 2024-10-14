class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [-1]* n
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()

        def bin_search(ele):
            left = 0
            right = n-1
            ans = float('inf')
            while left <= right:
                mid = (left+right) //2
                if(intervals[mid][0]>=ele):
                    ans = min(ans,mid)
                    right = mid -1
                else:
                    left = mid + 1
            return ans

        for i in intervals:
            val = bin_search(i[1])
            if val != float('inf'):
                res[i[2]] = intervals[val][2]
        return res
