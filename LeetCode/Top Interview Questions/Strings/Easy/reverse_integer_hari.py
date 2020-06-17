class Solution:
    def reverse(self, x: int) -> int:
        
        r = str(abs(x))[::-1]
        
        if x < 0:
            r = '-' + r
        
        r = int(r)
        
        if (r > 2**31) or r < (-1 * 2**31):
            return 0
        
        return int(r)
        
