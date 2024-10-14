class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=1
        if n == 1 :
            return 1
        while n:
            if n-k >=0:
                n-=k
                k+=1
            if n-k < 0:
                n=0
        return k-1
