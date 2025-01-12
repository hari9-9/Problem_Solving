class Solution:

    def solve(self, s1,s2,i,j,dp):
        if i == len(s1):
            return 0
        if j == len(s2):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        if s1[i]==s2[j]:
            ans = 1+ self.solve(s1,s2,i+1,j+1,dp)
        else:
            ans = max(self.solve(s1,s2,i+1,j,dp), self.solve(s1,s2,i,j+1,dp))
        dp[i][j] = ans
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        return self.solve(text1,text2,0,0,dp)
