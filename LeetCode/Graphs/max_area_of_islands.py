class Solution:

    def dfs(self,r,c,grid,visited):
        if (r<0 or r==len(grid) or c <0 or c==len(grid[0]) or grid[r][c] == 0 or (r,c) in visited):
            return 0
        visited.add((r,c))
        return (1 + self.dfs(r+1,c,grid,visited) + self.dfs(r-1,c,grid,visited)
        + self.dfs(r,c+1,grid,visited) + self.dfs(r,c-1,grid,visited))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area,self.dfs(r,c,grid,visited))
        return area
        
