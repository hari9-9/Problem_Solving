class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = []
        for num in nums:
            heapq.heappush(heap , - num)
        while k > 0:
            k-=1
            max_element =  - heapq.heappop(heap)
            ans +=max_element
            heapq.heappush(heap , -math.ceil(max_element / 3))

        return ans
        
