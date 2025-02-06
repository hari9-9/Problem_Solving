class Solution:

    def solve(self, s,i,j,dp):
        if i>j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if i == j:
            return 1
        ans = 0
        if s[i]==s[j]:
            ans = 2+self.solve(s,i+1,j-1,dp)
        else:
            ans = max(self.solve(s,i+1,j,dp) , self.solve(s,i,j-1,dp))
        dp[i][j] = ans
        return ans

    def longestPalindromeSubseq(self, s: str) -> int:
        i=0
        j= len(s)-1
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]
        return self.solve(s,i,j,dp)
        
