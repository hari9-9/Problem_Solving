class Solution:

    def dfs(self, i , j , grid , visited):
        if (i,j) in visited or i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]==0:
            return 0
        visited.add((i,j))
        return grid[i][j] + self.dfs(i+1,j,grid,visited) + self.dfs(i-1,j,grid,visited) + self.dfs(i,j+1,grid,visited) + self.dfs(i,j-1,grid,visited)


    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0 and (i,j) not in visited:
                    ans = max(ans , self.dfs(i,j,grid,visited))
        return ans

        
