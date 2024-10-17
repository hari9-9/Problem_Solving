class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <=right:
            if nums[left] > nums[right]:
                mid = (left+right) // 2
                if nums[mid] > nums[right]:
                    left= mid+1
                else:
                    right = mid
            else:
                return nums[left]
        return nums[left]
