class Solution:

    @staticmethod
    def solve(n,dp):
        if n==1 or n==0:
            dp[n]=n
            return n
        if dp[n] !=-1:
            return dp[n]
        dp[n] = Solution.solve(n-1,dp) + Solution.solve(n-2,dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        Solution.solve(n,dp)
        return dp[n]

############### Bottom UP Approach

class Solution:
    def fib(self, n: int) -> int:
        if n ==1 or n==0:
            return n
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp [i-1] + dp[i-2]
        return dp[n]
