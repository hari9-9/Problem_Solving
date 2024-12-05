class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = max_sum
        for i in nums[1:]:
            curr_sum = max(i+curr_sum,i)
            max_sum = max(curr_sum , max_sum)
        return max_sum
