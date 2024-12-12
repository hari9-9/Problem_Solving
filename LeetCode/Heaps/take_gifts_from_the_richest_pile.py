import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        print(gifts)
        heapq.heapify(gifts)
        ans = 0
        for i in range(k):
            pick = -(heapq.heappop(gifts))
            val = floor(sqrt(pick))
            ans += pick-val
            heapq.heappush(gifts,-val)
        return -sum(gifts)
