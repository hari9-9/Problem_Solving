class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bs(row):
            start = 0
            end = len(row)
            while start <end:
                mid = start+(end-start)//2
                if row[mid]<0:
                    end = mid
                else:
                    start = mid+1
            return len(row)-start

        count =0
        for row in grid:
            count+=bs(row)
        return count
