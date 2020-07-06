class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 3**int(round(log(n)/log(3))) == n if n>0 else False
