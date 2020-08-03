class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size() != t.size())
        {
            return false;
        }
        int len=s.size();
        int i;
        unordered_map <char , char> hmaps;
        unordered_map <char , char> hmapt;
        for(i=0;i<len;i++)
        {
            if(hmaps.find(s[i]) ==hmaps.end())
            {
                hmaps[s[i]]=t[i];
            }
            else
            {
                if(hmaps[s[i]] != t[i] )
                {
                    return false;
                }
            }
            if(hmapt.find(t[i]) ==hmapt.end())
            {
                hmapt[t[i]]=s[i];
            }
            else
            {
                if(hmapt[t[i]] != s[i] )
                {
                    return false;
                }
            }
        }
        return true;
        
        
    }
};
