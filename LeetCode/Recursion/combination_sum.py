class Solution:

    def solve(self,i,curr_sum,curr,ans,nums,target):
        if i >=len(nums):
            return
        if curr_sum == target:
            ans.append(curr.copy())
            return
        if curr_sum > target:
            return

        #exclude
        self.solve(i+1,curr_sum,curr,ans,nums,target)

        # include
        curr.append(nums[i])
        self.solve(i,curr_sum+nums[i],curr,ans,nums,target)
        curr.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        curr_sum = 0
        i=0
        self.solve(i,curr_sum,curr,ans,candidates,target)
        return ans
