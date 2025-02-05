class Solution:

    def solve(self,s,i,dp):
        if i in dp:
            return dp[i]
        if i == len(s):
            return 1
        if s[i]=='0':
            return 0
        count = self.solve(s,i+1,dp)
        if i+1 < len(s) and 10<=int(s[i:i+2])<=26:
            count+=self.solve(s,i+2,dp)
        dp[i] = count
        return count


    def numDecodings(self, s: str) -> int:
        dp = {}
        return self.solve(s,0,dp)
