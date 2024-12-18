class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >=prices[i]:
                ans[stack.pop()] -=prices[i]
            stack.append(i)

        return ans
