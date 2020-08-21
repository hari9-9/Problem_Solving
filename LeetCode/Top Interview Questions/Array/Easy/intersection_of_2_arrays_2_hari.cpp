class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map <int ,int> n1,n2;
        int i;
        for(i=0;i<nums1.size();i++)
        {
            if(n1.find(nums1[i]) == n1.end())
            {
                n1[nums1[i]]=1;
            }
            else
            {
                n1[nums1[i]]++;
            }
        }
        for(i=0;i<nums2.size();i++)
        {
            if(n2.find(nums2[i]) == n2.end())
            {
                n2[nums2[i]]=1;
            }
            else
            {
                n2[nums2[i]]++;
            }
        }
        vector<int> result;
        int n,j;
        for (auto i : n1)
        {
            if(n2.find(i.first) != n2.end())
            {
                //cout<<i.first<<' '<<i.second<<' '<<n2[i.first]<<endl;
                n=min(i.second , n2[i.first]);
                for(j=0;j<n;j++)
                {
                    result.push_back(i.first);
                }
            }
            // for(j=0;j<n;j++)
            // {
            //     result.push_back(i.first);
            // }
        }
        return result;
    }
};
