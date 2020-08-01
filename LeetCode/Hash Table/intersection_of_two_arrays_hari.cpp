class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int , bool>hset1;
        vector<int> res;
        int l=nums1.size();
        int i;
        for (i=0;i<l;i++)
        {
         hset1[nums1[i]]= true;    
        }
        l=nums2.size();
        for(i=0;i<l;i++)
        {
            if(hset1[nums2[i]])
            {
                res.push_back(nums2[i]);
                hset1[nums2[i]]= false;
                
            }
        }
        
        return res;
        
    }
};
