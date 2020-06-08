class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        values = dict()
        for i, elem  in enumerate(nums):
            compliment = target - elem
            if compliment in values:
                return [values[compliment],i]
            values[elem] = i
            
        return []
