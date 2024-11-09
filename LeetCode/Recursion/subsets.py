from typing import List

class Solution:
    def solver(self, nums: List[int], ans: List[List[int]], output: List[int], i: int):
        if i == len(nums):
            ans.append(output.copy())
            return

        # Exclude the current element
        self.solver(nums, ans, output, i + 1)

        # Include the current element
        output.append(nums[i])
        self.solver(nums, ans, output, i + 1)
        output.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        output = []
        i = 0
        self.solver(nums, ans, output, i)
        return ans
