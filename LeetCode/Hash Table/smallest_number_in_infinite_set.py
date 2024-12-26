class SmallestInfiniteSet:
    def __init__(self):
        self.popped_elements = set()

    def popSmallest(self) -> int:
        smallest = 1
        while smallest in self.popped_elements:
            smallest += 1
        self.popped_elements.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.popped_elements:
            self.popped_elements.remove(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
