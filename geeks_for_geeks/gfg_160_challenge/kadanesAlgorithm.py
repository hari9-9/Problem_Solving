#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,nums):
        ##Your code here
        max_sum = nums[0]
        curr_sum = max_sum
        for i in nums[1:]:
            curr_sum = max(i+curr_sum,i)
            max_sum = max(curr_sum , max_sum)
        return max_sum
        
