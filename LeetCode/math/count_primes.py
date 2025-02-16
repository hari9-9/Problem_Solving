class Solution:
    def countPrimes(self, n: int) -> int:
        primes =  [True] * n
        ans = 0
        for i in range(2,n):
            if primes[i]:
                ans+=1
            curr = i+i
            while(curr<n):
                primes[curr] = False
                curr+=i
        return ans
