class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        for _ in range(k):
            ele, idx = heapq.heappop(heap)
            nums[idx] = ele*multiplier
            heapq.heappush(heap,(ele*multiplier,idx))
        return nums
        
