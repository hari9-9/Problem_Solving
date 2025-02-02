class Solution:
    def check(self, nums: List[int]) -> bool:
        inv = 0
        if len(nums)==1:
            return True
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                inv+=1

        if nums[-1] > nums[0]:
            inv+=1
        return inv<=1
