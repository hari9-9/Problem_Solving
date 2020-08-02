class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int , int>hmap;
        vector<int> ans;
        int len = nums.size();
        int i;
        int c;
        for(i=0;i<len;i++)
        {
            c=target-nums[i];
            if(hmap.find(c)!=hmap.end())
            {
                ans.push_back(hmap.find(c)->second);
                ans.push_back(i);
                break;
            }
            else
                hmap[nums[i]]=i;
        }
        return ans;
        
        
    }
};
