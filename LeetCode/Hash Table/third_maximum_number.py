class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hash = set()
        for i in nums:
            hash.add(i)

        i=0
        ans = 0
        if len(hash)<3:
            return max(hash)
        while hash and i<2:
            hash.remove(max(hash))
            i+=1
        return max(hash)
