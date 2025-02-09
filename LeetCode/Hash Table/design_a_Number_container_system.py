class NumberContainers:

    def __init__(self):
        self.num = {}
        self.ind = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        temp = None
        if index in self.num:
            temp = self.num[index]
        self.num[index] = number
        if temp:
            self.ind[temp].remove(index)
            if not self.ind[temp]:
                del self.ind[temp]
        self.ind[number].add(index)

    def find(self, number: int) -> int:
        if number in self.ind and self.ind[number]:
            return self.ind[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
