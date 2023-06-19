class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp = nums[i]
                nums[i] = nums[slow]
                nums[slow] = temp
                slow += 1








class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[slow] = nums[i]
                slow += 1
        for i in range(slow,len(nums)):
            nums[i] = 0




# bad runtime , but good memory 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if (i==0):
                nums.remove(i)
                nums.append(i)
        return nums
    


# python optimized 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return -1
    
        zeroes = nums.count(0) 
        
        nums[:] = [num for num in nums if num != 0]
        nums += [0] * zeroes