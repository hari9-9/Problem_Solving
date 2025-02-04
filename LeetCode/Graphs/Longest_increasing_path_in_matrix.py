class Solution:

    def dfs(self,i,j,matrix,dp,prev):
        if not 0<=i<len(matrix) or not 0<=j<len(matrix[0]):
            return 0
        if matrix[i][j] <= prev:
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        res = 1
        res = max(res , 1+self.dfs(i+1,j,matrix,dp,matrix[i][j]))
        res = max(res , 1+self.dfs(i-1,j,matrix,dp,matrix[i][j]))
        res = max(res , 1+self.dfs(i,j+1,matrix,dp,matrix[i][j]))
        res = max(res , 1+self.dfs(i,j-1,matrix,dp,matrix[i][j]))
        dp[(i,j)] = res
        return dp[(i,j)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(i,j,matrix,dp,-1)
        return max(dp.values())
