# Botoom UP
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            print("TO MAKE AMOUNT "+ str(i))
            for j in range(len(coins)):
                print("taking coin with value "+ str(coins[j]))
                if i-coins[j] >=0 and dp[i-coins[j]] != float('inf'):
                    print("amount - current coin "+ str(i-coins[j]))
                    print(dp[i-coins[j]])
                    dp[i] = min(dp[i],1+dp[i-coins[j]])
                    print(dp)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]




# Top Down
# class Solution:
#     @staticmethod
#     def solve(coins,amount,dp):
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return float('inf')
#         if dp[amount] !=-1:
#             return dp[amount]
#         mini = float('inf')
#         for i in range(len(coins)):
#             ans = Solution.solve(coins, amount - coins[i],dp)
#             if ans != float('inf'):
#                 mini = min(mini,1+ans)
#         dp[amount] = mini
#         return mini
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [-1]*(amount+1)
#
#         ans = Solution.solve(coins,amount,dp)
#         if ans == float('inf'):
#             return -1
#         else:
#             return ans

# class Solution:
#     @staticmethod
#     def solve(coins,amount):
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return float('inf')
#         mini = float('inf')
#         for i in range(len(coins)):
#             ans = Solution.solve(coins, amount - coins[i])
#             if ans != float('inf'):
#                 mini = min(mini,1+ans)
#         return mini
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         ans = Solution.solve(coins,amount)
#         if ans == float('inf'):
#             return -1
#         else:
#             return ans
