class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums[0] < k and len(nums)>=2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            curr = min(x,y) * 2 + max(x,y)
            heapq.heappush(nums,curr)
            operations +=1
        return operations
        
