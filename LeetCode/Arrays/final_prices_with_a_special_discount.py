class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        disc = []
        for i in range(len(prices)):
            curr = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j]<=curr:
                    curr-=prices[j]
                    break
            disc.append(curr)
        return disc
