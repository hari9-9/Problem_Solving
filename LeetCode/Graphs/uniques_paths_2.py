class Solution:

    def solve(self,i,j,grid,dp):
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if grid[i][j]:
            dp[i][j] = 0
            return 0
        res = self.solve(i-1,j,grid,dp)+ self.solve(i,j-1,grid,dp)
        dp[i][j] = res
        return res

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        # Initialize the first row
        for i in range(n):  # Fix loop to iterate over columns
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        # Initialize the first column
        for i in range(m):  # Fix loop to iterate over rows
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        return self.solve(len(obstacleGrid)-1 , len(obstacleGrid[0])-1 , obstacleGrid,dp)
