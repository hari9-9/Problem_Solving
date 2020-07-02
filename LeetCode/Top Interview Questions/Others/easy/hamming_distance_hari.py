class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_prod = x^y
        ans=0
        while(xor_prod):
            ans+=xor_prod & 1
            xor_prod = xor_prod>>1
        return ans
    
