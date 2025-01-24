class Solution:

    def bfs(self,r,c,grid, visited):
        q = []
        visited.add((r,c))
        q.append((r,c))

        while q:
            rp , cp = q.pop(0)
            dir = [[0,1],[-1,0],[1,0],[0,-1]]
            for dr , dc in dir:
                row = rp + dr
                col = cp + dc
                if (row in range(len(grid)) and
                    col in range(len(grid[0])) and
                    grid[row][col] == "1" and
                    (row,col) not in visited):

                    q.append((row,col))
                    visited.add((row,col))


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.bfs(r,c,grid,visited)
                    ans+=1
        return ans



class Solution:

    def dfs(self,i,j,visited,grid):
        if i>=len(grid) or j >=len(grid[0]):
            return
        if (i,j) in visited:
            return
        visited.add((i,j))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        for dx , dy in dirs:
            if 0<=i+dx<len(grid) and 0<=j+dy<len(grid[0]) and grid[i+dx][j+dy]=='1':
                self.dfs(i+dx , j+dy , visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and ((i,j) not in visited):
                    self.dfs(i,j,visited,grid)
                    ans+=1
        return ans
