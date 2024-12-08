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
        
