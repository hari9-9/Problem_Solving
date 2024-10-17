class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)




#



class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #k = k % len(nums)
        n = len(nums)
        k = k %n
        # while k:
        #     temp = nums[-1]
        #     for i in range(len(nums)-1,0,-1):
        #         nums[i] , nums[i-1] = nums[i-1] , nums[i]
        #     nums[0] = temp
        #     k-=1
        # for i in range(k):
        #     nums.insert(0, nums.pop())
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)


        
