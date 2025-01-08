class Solution:

    def solve(self, nums, target):
        if target < 0:
            return 0
        if target ==0:
            return 1
        ans = 0
        for i in range(len(nums)):
            ans+= self.solve(nums,target-nums[i])
        return ans

    def combinationSum4(self, nums: List[int], target: int) -> int:

        ans = self.solve(nums , target)
        return ans


# recursion top down:
class Solution:

    def solve(self, nums, target,dp):
        if target < 0:
            return 0
        if target ==0:
            return 1
        if dp[target] != -1:
            return dp[target]
        ans = 0
        for i in range(len(nums)):
            ans+= self.solve(nums,target-nums[i],dp)

        dp[target] = ans
        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1]* (target+1)
        ans = self.solve(nums , target,dp)
        return ans
