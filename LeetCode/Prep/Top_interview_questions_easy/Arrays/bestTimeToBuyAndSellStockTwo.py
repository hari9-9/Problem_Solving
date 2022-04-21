class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        b=prices[0]
        s=prices[0]
        total =0
        while i<len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            b=prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
            s=prices[i]
            total+= s-b
        
        return total
