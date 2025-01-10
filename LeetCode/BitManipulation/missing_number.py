class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all = 0
        xor_list = 0
        for i in range(len(nums)+1):
            xor_all ^= i
        for i in nums:
            xor_list ^= i
        return xor_all ^ xor_list
