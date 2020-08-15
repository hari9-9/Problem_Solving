class Solution {
public:
    int numJewelsInStones(string J, string S) {
        unordered_set<char> hset;
        int len=J.length();
        int i;
        for(i=0;i<len;i++)
        {
            if(hset.find(J[i])==hset.end())
            {
                hset.insert(J[i]);
            }
        }
        len=S.length();
        int count=0;
        for(i=0;i<len;i++)
        {
            if(hset.find(S[i])!=hset.end())
            {
                count++;
            }
        }
        return count;
        
    }
};
