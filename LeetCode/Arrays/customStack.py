class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.top = -1
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.top+=1
        

    def pop(self) -> int:
        if len(self.stack):
            self.top-=1
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.stack)):
            if i<k:
                self.stack[i]+=val
            else:
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)