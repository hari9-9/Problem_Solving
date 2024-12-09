# Recursive
class Solution:
    @staticmethod
    def solve(coins,amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        mini = float('inf')
        for i in range(len(coins)):
            ans = Solution.solve(coins, amount - coins[i])
            if ans != float('inf'):
                mini = min(mini,1+ans)
        return mini
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = Solution.solve(coins,amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
