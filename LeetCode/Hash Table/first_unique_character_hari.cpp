class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map <char ,int> hmap;
        unordered_map <char ,int> hmap_ind;
        int l = s.length();
        int i;
        for(i=0;i<l;i++)
        {
            if(hmap.find(s[i]) ==hmap.end())
            {
                hmap[s[i]]=1;
                hmap_ind[s[i]] = i;
                
            }
            else
            {
                hmap[s[i]]++;
            }
        }
        int m=INT_MAX;
        bool flag= false;
        for (auto i = hmap.begin(); i != hmap.end(); i++)
        {
            if(i->second == 1 && hmap_ind[i->first]<m)
            {
                flag=true;
                m=hmap_ind[i->first];
            }
        }
        if(flag == false)
            return -1;
     return m;   
    }
};
