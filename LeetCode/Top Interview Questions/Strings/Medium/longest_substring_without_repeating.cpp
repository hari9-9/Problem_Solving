class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char>hset;
        int i=0;
        int j=0;
        int ans=0;
        int l =s.length();
        while(i<l &&j<l)
        {
            if(hset.find(s[j])==hset.end())
            {
                hset.insert(s[j++]);
                ans = max(ans,j-i);
            }
            else
            {
                hset.erase(s[i++]);
            }
        }
        return ans;
   
