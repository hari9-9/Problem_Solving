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
