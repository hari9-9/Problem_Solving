class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        max_right = [0]*n
        max_right[n-1] = n-1
        for i in range(n-2,-1,-1):
            if nums[i] > nums[max_right[i+1]]:
                max_right[i] = i
            else:
                max_right[i] = max_right[i+1]

        for i in range(n):
            if nums[i] < nums[max_right[i]]:
                nums[i], nums[max_right[i]] = (
                    nums[max_right[i]],
                    nums[i],
                )
                return int("".join(nums))
        return num
        
