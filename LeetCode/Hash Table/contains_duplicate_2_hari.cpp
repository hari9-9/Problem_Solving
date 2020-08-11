class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        
        unordered_map <int ,int > hmap;
        int i;
        for(i=0;i<nums.size();i++)
        {
            if(hmap.find(nums[i])!=hmap.end())
            {
                if(i-hmap[nums[i]]<=k)
                {
                    return true;
                }
                else
                {
                    hmap[nums[i]]=i;
                }
            }
            else
            {
               hmap[nums[i]]=i; 
            }
        }
        return false;
        
    }
};
