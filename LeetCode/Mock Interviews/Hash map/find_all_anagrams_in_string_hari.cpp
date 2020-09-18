class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if(p.size()==0|| s.size()==0)
        {
            return{};
        }
        vector<int> v{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
        unsigned long long int req,curr;
        int plen =p.size();
        req=1;
        int i;
        vector<int>ans;
        curr=1;
        for(i=0;i<plen;i++)
        {
            req*=v[char(p[i])-97];
        }
        cout<<req<<endl;
        for(i=0;i<plen;i++)
        {
            curr*=v[char(s[i])-97];    
        }
        cout<<curr<<endl;
        for(i=plen;i<s.size();i++)
        {
            if(curr==req)
                ans.push_back(i-plen);
            curr/=v[char(s[i-plen])-97];
            curr*=v[char(s[i])-97];
        }
        if(curr==req)
            ans.push_back(i-plen);
        return ans;
    }
};

// hmap based solution 
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> dp, tmp;
        for (int i = 0; i < p.size(); ++i) 
            dp[p[i]]++;
        for (int i = 0; i < p.size(); ++i) {
            tmp[s[i]]++;
        }
        vector<int> ans;
        if (tmp == dp) ans.push_back(0);
        
        for (int i = p.size(); i < s.size(); ++i) {
            if (tmp[s[i - p.size()]] == 1) 
                tmp.erase(s[i - p.size()]);
            else 
                tmp[s[i - p.size()]]--;
            tmp[s[i]]++;
            if (tmp == dp) 
                ans.push_back(i - p.size() + 1);
        }
        return ans;
    }
};
