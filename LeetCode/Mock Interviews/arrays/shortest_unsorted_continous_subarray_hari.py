class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=nums.copy()
        l.sort()
        print(l)
        print(nums)
        start=len(nums)
        stop=0
        for i in range(len(nums)):
            if(l[i]!=nums[i]):
                start=min(start,i)
                stop=max(stop,i)
        if(stop-start>=0):
            return stop-start+1
        else:
            return 0
