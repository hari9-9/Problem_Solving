class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==0 or len(nums) ==1:
            return True
        can = [False]*len(nums)
        can[0] = True
        for i in range(len(nums)):
            if can[i]:
                curr = nums[i]
                for j in range(1,curr+1):
                    if i+j < len(nums):
                        can[i+j] = True
            if can[-1]:
                return True
        return can[-1]
        
