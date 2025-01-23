class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])
        rowc = [0]*row
        colc = [0]*col
        for i in range(row):
            for j in range(len(grid[0])):
                rowc[i]+=grid[i][j]

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                colc[i] += grid[j][i]

        print(rowc)
        print(colc)
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if rowc[i]>1 or colc[j]>1:
                        ans+=1
        return ans
