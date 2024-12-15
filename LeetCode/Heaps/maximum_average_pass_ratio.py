class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gaincalc(pas,tot):
            return ((pas+1) / (tot+1)) - (pas/tot)

        heap = []
        for pas,tot in classes:
            gain = gaincalc(pas,tot)
            heapq.heappush(heap , (-gain,pas,tot))
        for _ in range(extraStudents):
            g,p,t = heapq.heappop(heap)
            heapq.heappush(heap,(-gaincalc(p+1,t+1),p+1,t+1))

        ans = 0
        while heap:
            g,p,t = heapq.heappop(heap)
            ans+=p/t
        return ans/len(classes)

        
