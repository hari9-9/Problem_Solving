class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        mid = float('inf')
        for n in nums:
            if n > mid:
                return True
            if n<=small:
                small = n
            else:
                mid = n
        return False
