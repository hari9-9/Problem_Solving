class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # nums = nums.sort()
        hashset = set()
        for i in nums:
            hashset.add(i)
        maxval = -1
        found = False
        for i in nums:
            curr = 0
            val = i
            while (val*val) in hashset:
                val = val*val
                # Break if the next square would be larger than 10^5 (problem constraint)
                if val > 10**5:
                    break
                curr+=1
                found = True
            maxval = max(curr,maxval)
        if found:
            return maxval+1
        else:
            return -1
        
