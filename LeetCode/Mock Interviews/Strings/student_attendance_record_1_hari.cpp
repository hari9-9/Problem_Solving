class Solution {
public:
    bool checkRecord(string s) {
        int n =s.size();
        int i=0;
        int a=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='A')
            {
                a++;
                if(a>1)
                {
                    return false;
                }
            }
        }
        for(i=0;i<n-2;i++)
        {
            if(s[i]=='L' && s[i+1]=='L' && s[i+2]=='L')
                return false;
        }
        return true;
        
    }
};
