## Recursion
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

## TOp Down:

# class Solution:

#     @staticmethod
#     def solve(nums,idx,dp):
#         if idx<0:
#             return 0
#         if idx ==0:
#             return nums[0]
#         if dp[idx] != -1:
#              return dp[idx]
#         incl = Solution.solve(nums,idx-2,dp) + nums[idx]
#         exl = Solution.solve(nums,idx-1,dp)
#         dp[idx] = max(incl,exl)
#         return dp[idx]



#     def rob(self, nums: List[int]) -> int:
#         dp = [-1]*len(nums)
#         ans = Solution.solve(nums,len(nums)-1,dp)
#         return ans

## Bottum UP:
class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) ==2:
            return max(nums[0],nums[1])
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            incl = dp[i-2]+ nums[i]
            exc = dp[i-1]
            dp[i] = max(incl,exc)
        return dp[-1]
















# class Solution:

#     @staticmethod
#     def solve(nums,idx,ans):
#         if idx<0:
#             return ans
#         if idx ==0:
#             return ans+nums[0]

#         incl = Solution.solve(nums,idx-2,ans+nums[idx])
#         exl = Solution.solve(nums,idx-1,ans)
#         return max(incl,exl)



#     def rob(self, nums: List[int]) -> int:
#         ans = Solution.solve(nums,len(nums)-1,0)
#         return ans


# class Solution:

#     @staticmethod
#     def solve(nums,idx,ans,dp):
#         if idx<0:
#             return 0
#         if dp[idx] != -1:
#             return dp[idx]
#         incl = Solution.solve(nums,idx-2,ans+nums[idx],dp)
#         exl = Solution.solve(nums,idx-1,ans,dp)
#         dp[idx] = max(incl,exl)
#         return dp[idx]



#     def rob(self, nums: List[int]) -> int:
#         dp = [-1]*len(nums)
#         ans = Solution.solve(nums,len(nums)-1,0,dp)
#         return ans
        
