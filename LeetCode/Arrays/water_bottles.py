class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emp = 0
        while numBottles:
            ans+=numBottles
            emp+=numBottles
            numBottles = emp // numExchange
            emp = emp % numExchange
        return ans
