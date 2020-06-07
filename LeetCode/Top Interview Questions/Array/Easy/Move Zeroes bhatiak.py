"""
this is my original solution.
Runtime: 52 ms
Memory Usage: 15 MB
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        i=0
        while(i<len(nums)):
            if nums[i]==0:
                nums.pop(i)
                count+=1
                i-=1
            i+=1
        nums.extend([0]*count)
