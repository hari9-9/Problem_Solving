class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        ans = 0
        while n:
            if n & mask:
                ans+=1
            n = n>>1
        return ans
