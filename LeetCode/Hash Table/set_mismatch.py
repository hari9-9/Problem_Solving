class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = set()
        n = len(nums)
        ans1 = -1
        ans2 = -1
        for i in nums:
            if i in hash:
                ans1 = i
            else:
                hash.add(i)
        for i in range(1,n+1):
            if i not in hash:
                ans2 = i
                break
        return [ans1,ans2]
        
