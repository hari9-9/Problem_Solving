class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s=0
        z=0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            while z>1:
                if nums[s]==0:
                    z-=1
                s+=1
            ans = max(ans,i-s)
        return ans
