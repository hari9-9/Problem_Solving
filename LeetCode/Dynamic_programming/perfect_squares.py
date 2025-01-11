class Solution:

    def solve(self , n):
        if n ==0 :
            return 0
        ans = n
        i=1
        while i*i<=n:
            ans = min(ans , 1+self.solve(n-(i*i)))
            i+=1
        return ans

    def numSquares(self, n: int) -> int:
        return self.solve(n)



top down memo:
class Solution:

    def solve(self , n,dp):
        if n == 0 :
            return 0
        if dp[n] !=-1:
            return dp[n]
        ans = n
        i=1
        while i*i<=n:
            ans = min(ans , 1+self.solve(n-(i*i),dp))
            i+=1
        dp[n] = ans
        return dp[n]

    def numSquares(self, n: int) -> int:
        dp = [-1]* (n+1)
        return self.solve(n,dp)
