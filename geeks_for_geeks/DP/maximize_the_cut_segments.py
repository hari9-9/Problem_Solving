#Recursive

class Solution:

    def solve(self,n,x,y,z):
        if n ==0:
            return 0
        if n <0:
            return float('-inf')
        a = self.solve(n-x,x,y,z)+1
        b = self.solve(n-y,x,y,z)+1
        c = self.solve(n-z,x,y,z)+1
        return max(a,max(b,c))

    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        ans = self.solve(n,x,y,z)
        if ans<0:
            return 0
        return ans

# top down :
class Solution:

    def solve(self,n,x,y,z,dp):
        if n ==0:
            return 0
        if n <0:
            return float('-inf')
        if dp[n] != -1:
            return dp[n]
        a = self.solve(n-x,x,y,z,dp)+1
        b = self.solve(n-y,x,y,z,dp)+1
        c = self.solve(n-z,x,y,z,dp)+1
        dp[n] = max(a,max(b,c))
        return dp[n]

    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [-1]*(n+1)
        ans = self.solve(n,x,y,z,dp)
        if ans<0:
            return 0
        return ans
