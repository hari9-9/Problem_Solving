class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            curr = nums[i]
            left = i+1
            right = len(nums)-1
            while left<len(nums) and right>i and left<right:
                if curr+nums[left]+nums[right] == 0:
                    ans.append([curr , nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left <right and nums[right]==nums[right-1]:
                        right -=1
                if curr+nums[left]+nums[right] > 0:
                    right-=1
                else:
                    left+=1
        return ans
