class Solution:
    def tribonacci(self, n: int) -> int:
        if n <3:
            dp = [0]*3
        else:
            dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        if n <3:
            return dp[n]
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp)
        return dp[n]


        
