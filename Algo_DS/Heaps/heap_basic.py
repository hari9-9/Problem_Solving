class Heaps:
    def __init__(self):
        self.h = []
        self.h.append(-1)
        self.size = 0

    def insert(self, val):
        self.size += 1
        self.h.append(val)
        index= self.size
        while index > 1:
            parent = index //2
            if(self.h[parent] < self.h[index]):
                self.h[parent] , self.h[index] = self.h[index] , self.h[parent]
                index = parent
            else:
                return

    def delete(self):
        if self.size == 0:
            return
        self.h[1] = self.h[self.size]
        self.size-=1
        i=1
        while i <self.size:
            left = 2*i
            right = 2*i+1
            if left<self.size and self.h[i] < self.h[left]:
                self.a[left] , self.a[i] = self.a[i] , self.a[left]
                i=left
            elif right<self.size and self.h[i] < self.h[right]:
                self.a[right] , self.a[i] = self.a[i] , self.a[right]
                i=right

    def printHeap(self):
        print(self.h[1:self.size+1])


heap = Heaps()
heap.insert(10)
heap.insert(20)
heap.printHeap()
heap.delete()
heap.printHeap()
