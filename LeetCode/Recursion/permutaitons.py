class Solution:
    @staticmethod
    def solve(nums,idx,ans):
        if idx >=len(nums):
            ans.append(nums.copy())
            return
        for i in range(idx,len(nums)):
            nums[idx] , nums[i] = nums[i] , nums[idx]
            Solution.solve(nums,idx+1,ans)
            nums[idx] , nums[i] = nums[i] , nums[idx]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        Solution.solve(nums,0,ans)
        return ans
