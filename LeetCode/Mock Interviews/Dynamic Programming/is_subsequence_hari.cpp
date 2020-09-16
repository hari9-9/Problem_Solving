class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.size()==0 && t.size()==0)
        {
            return true;
        }
        int dp[t.size()+1];
        memset(dp,0,sizeof(dp));
        int i=0;
        int curr=0;
        if(t[i]==s[curr])
        {
            dp[0]=1;
            curr++;
        }
        if(curr==s.size())
        {
            return true;
        }
        for(i=1;i<t.size();i++)
        {
            //cout<<i<<s[i]<<t[curr]<<endl;
            if(t[i]==s[curr])
            {
                dp[i]=dp[i-1]+1;
                //cout<<dp[i]<<endl;
                curr++;
            }
            if(curr==s.size())
            {
                return true;
            }
        }
        return false;
        
    }
};
