class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i] =1
        heap = []
        for num , freq in hash.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        ans = []
        for freq,num in heap:
            ans.append(num)
        return ans
