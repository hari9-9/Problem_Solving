class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heap.append((-stones[i] , -i))
        heapq.heapify(heap)
        i = len(stones)
        while len(heap) > 1:
            y , _ = heapq.heappop(heap)
            x , _ = heapq.heappop(heap)
            x*=-1
            y*=-1
            if x == y :
                continue
            heapq.heappush(heap , (-1*(y-x) , -i))
            i+=1
        if len(heap):
            return -1*heap[0][0]
        return 0
