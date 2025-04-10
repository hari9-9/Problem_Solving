class Solution:
    def solve(self, nums, i, end, dp):
        if i > end:
            return 0
        if i in dp:
            return dp[i]
        
        dp[i] = max(
            self.solve(nums, i + 1, end, dp),
            nums[i] + self.solve(nums, i + 2, end, dp)
        )
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp1 = {}
        dp2 = {}

        case1 = self.solve(nums, 0, n - 2, dp1)
        case2 = self.solve(nums, 1, n - 1, dp2)

        return max(case1, case2)