class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = -1
        res = [False] * len(candies) 
        for i in range(len(candies)):
            if candies[i] > high :
                high = candies[i]
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= high:
                res[i] = True
        
        return res