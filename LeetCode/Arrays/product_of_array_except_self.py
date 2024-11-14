class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(1,len(nums)):
            left.append(nums[i-1]*left[-1])
        print(left)
        for i in range(len(nums)-2,-1,-1):
            #right.append(nums[i]*right[-1])
            # print(nums[i])
            # print(right[i-1])
            right.insert(0,nums[i+1]*right[0])
        print(right)
        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        return ans
