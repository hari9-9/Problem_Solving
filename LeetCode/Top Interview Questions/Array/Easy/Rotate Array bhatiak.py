"""
this is my original solution without checking the provided solution. 
space: 15.5 MB 
time: 192 ms

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k= k-l*(int(k/l))
        for i in range(k):
            nums.insert(0, nums.pop())
