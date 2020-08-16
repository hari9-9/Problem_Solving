class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len=s.length();
        unordered_set<char> hset;
        int i=0,j=0,ans=0;
        while(i<len && j<len )
        {
            if(hset.find(s[j])==hset.end())
            {
                hset.insert(s[j++]);
                ans=std :: max(ans,j-i);
            }
            else
            {
                hset.erase(s[i++]);
            }
        }
        return ans;
        
    }
};
