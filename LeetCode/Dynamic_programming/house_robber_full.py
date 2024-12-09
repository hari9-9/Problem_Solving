# class Solution:

#     @staticmethod
#     def solve(nums,idx):
#         if idx<0:
#             return 0
#         if idx ==0:
#             return nums[0]

#         incl = Solution.solve(nums,idx-2) + nums[idx]
#         exl = Solution.solve(nums,idx-1)
#         return max(incl,exl)



#     def rob(self, nums: List[int]) -> int:
#         ans = Solution.solve(nums,len(nums)-1)
#         return ans

class Solution:

    @staticmethod
    def solve(nums,idx,ans):
        if idx<0:
            return ans
        if idx ==0:
            return ans+nums[0]

        incl = Solution.solve(nums,idx-2,ans+nums[idx])
        exl = Solution.solve(nums,idx-1,ans)
        return max(incl,exl)



    def rob(self, nums: List[int]) -> int:
        ans = Solution.solve(nums,len(nums)-1,0)
        return ans
