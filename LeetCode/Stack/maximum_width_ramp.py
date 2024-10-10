class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        width = 0

        for i in range(len(nums)-1 , -1 , -1):
            while stack and nums[stack[-1]] <= nums[i]:
                width = max(width , i-stack[-1])
                stack.pop()

        return width
