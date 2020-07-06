# Sieve of Eratosthenes method.
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n in (0, 1): return 0

        lst = [0 for i in range(n)]
        lst[0] = 1
        lst[1] = 1

        count=0
        for p in range(2, n):
            if lst[p] != 1:
                count+=1
                for i in range(p*p, n, p):
                    if i%p == 0:
                        lst[i] = 1
                # lst[p*p:n:p] = [1 if i%p == 0 else 0 for i in range(p*p, n, p)] # Super short form of last 3 lines XD.

        return count
