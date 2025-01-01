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

        
