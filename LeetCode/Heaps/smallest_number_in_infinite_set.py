import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.curr = 1
        self.added = set()  # To track added elements

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added.remove(smallest)  # Remove from added set
            return smallest
        else:
            ans = self.curr
            self.curr += 1
            return ans

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)  # Track the added element
