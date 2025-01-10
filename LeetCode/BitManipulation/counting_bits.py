class Solution:
    def solve(self,n):
        mask = 1
        ans= 0
        while n:
            if n & mask:
                ans+=1
            n = n>>1
        return ans
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(len(ans)):
            ans[i] = self.solve(i)
        return ans



class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        off = 1
        for i in range(1,n+1):
            if off *2 == i:
                off=i
            dp[i] = 1+ dp[i-off]
        return dp
