class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = []
        mins = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh>0:
            mins+=1
            for _ in range(len(q)):
                r , c = q.pop(0)
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dx ,dy in directions:
                    if 0<=r+dx<len(grid) and 0<=c+dy<len(grid[0]) and grid[r+dx][c+dy]==1:
                        fresh-=1
                        grid[r+dx][c+dy] = 2
                        q.append((r+dx , c+dy))
        if fresh==0:
            return mins
        else:
            return -1
