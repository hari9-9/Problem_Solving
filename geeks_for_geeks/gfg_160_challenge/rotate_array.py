#User function Template for python3

class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, nums, k):
        #Your code here
        n = len(nums)
        # k=k+1
        k %= n

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)
        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
