############ Bottom UP:
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
        return min(dp[n-1] , dp[n-2])






#########3 TOp Down

# class Solution:
#     @staticmethod
#     def solve(cost,n,dp):
#         if n==0:
#             return cost[0]
#         if n==1:
#             return cost[1]
#         if dp[n] != -1:
#             return dp[n]

#         dp[n] =  cost[n] + min(Solution.solve(cost,n-1,dp), Solution.solve(cost,n-2,dp))
#         return dp[n]

#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dp = [-1] * (n+1)
#         return min(Solution.solve(cost,n-1,dp) , Solution.solve(cost, n-2,dp))





# class Solution:
#     @staticmethod
#     def solve(cost,n):
#         if n==0:
#             return cost[0]
#         if n==1:
#             return cost[1]
#         return cost[n] + min(Solution.solve(cost,n-1), Solution.solve(cost,n-2))

#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         return min(Solution.solve(cost,n-1) , Solution.solve(cost, n-2))
