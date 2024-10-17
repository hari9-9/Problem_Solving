class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash ={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in hash:
            if hash.get(i) == 1:
                return i
        return 0
