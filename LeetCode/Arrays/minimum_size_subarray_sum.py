class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        csum = 0
        curr_min = float('inf')
        left = 0
        for right in range(len(nums)):
            csum+=nums[right]
            while csum >= target:
                curr_min = min(curr_min , right-left+1)
                csum -=nums[left]
                left+=1

        return 0 if curr_min == float('inf') else curr_min


        
