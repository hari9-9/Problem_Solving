class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profit = 0
        while i<len(prices)-1:
            while i+1 < len(prices) and prices[i] >= prices[i+1]:
                i+=1
            buy = prices[i]
            while i+1 <len(prices) and prices[i] <= prices[i+1]:
                i+=1
            profit += prices[i]-buy
        return profit
        
