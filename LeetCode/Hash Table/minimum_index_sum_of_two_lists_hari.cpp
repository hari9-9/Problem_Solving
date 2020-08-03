class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string , int> andy;
        unordered_map<string , int> doris;
        vector<string> ans;
        int len=list1.size();
        int i;
        for(i=0;i<len;i++)
        {
            andy[list1[i]]=i;
        }
        len=list2.size();
        for(i=0;i<len;i++)
        {
            doris[list2[i]]=i;
        }
        len=2001;
        unordered_map<string , int> com;
        for(auto it=andy.begin();it!=andy.end();it++) 
        {
            //cout<<it->first <<endl;
            if(doris.find(it->first) != doris.end())
            {
                com[it->first] = it->second + doris[it->first];
                if((it->second + doris[it->first]) < len)
                {
                    len=it->second +doris[it->first];
                    //cout<<len<<endl;
                }
            }
            //cout<<(it->first); 
        }
        for(auto it=com.begin();it!=com.end();it++)
        {
            if(it->second == len)
            {
                ans.push_back(it->first);
            }
                       
        }
        
        
        return ans;
    }
};
