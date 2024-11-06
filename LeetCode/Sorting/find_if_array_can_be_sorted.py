class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = nums.copy()
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] <= arr[j+1]:
                    continue
                else:
                    if bin(arr[j]).count('1') == bin(arr[j+1]).count('1'):
                        arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    else:
                        return False
        return True 
