class Solution:
    def fibR(self , n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibR(n-1) + self.fibR(n-2)
    def fib(self, n: int) -> int:
        return self.fibR(n)
