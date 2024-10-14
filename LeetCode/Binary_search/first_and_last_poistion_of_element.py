class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        left = 0
        right = len(nums)-1
        while left <= right:
            mid= (left+right)//2
            if nums[mid] == target:
                l = mid
                r=mid
                while  l>=0 and nums[l] == target:
                    l-=1
                while r<=len(nums)-1 and nums[r] == target:
                    r+=1
                return [l+1,r-1]
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [-1,-1]
