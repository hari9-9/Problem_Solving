class Solution {
public:
    int hammingWeight(uint32_t n) {
        int mask=1;
        int bits=0;
        int i;
        while(n)
        {
            if(n&1)
            {
                bits++;
            }
            n>>=1;
        }
        return bits;
        
    }
};
