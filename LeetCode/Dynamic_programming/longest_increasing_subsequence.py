class Solution:
    def solve(self, nums, curr, prev, dp):
        if curr == len(nums):  # Base case: No more elements to process
            return 0
        if dp[curr][prev + 1] != -1:  # If already computed, return the cached value
            return dp[curr][prev + 1]

        # Option 1: Include nums[curr] if it's greater than nums[prev]
        take = 0
        if prev == -1 or nums[curr] > nums[prev]:
            take = 1 + self.solve(nums, curr + 1, curr, dp)

        # Option 2: Skip nums[curr]
        dont = self.solve(nums, curr + 1, prev, dp)

        # Store the result in dp and return
        dp[curr][prev + 1] = max(take, dont)
        return dp[curr][prev + 1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Initialize dp with -1, size (n x (n + 1)) because prev can be -1 to n-1
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.solve(nums, 0, -1, dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)-1 , -1 , -1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
