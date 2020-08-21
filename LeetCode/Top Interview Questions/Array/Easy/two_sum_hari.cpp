class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>ans;
        unordered_map<int, int> hset;
        int i,l;
        l=nums.size();
        for(i=0;i<l;i++)
        {
            if(hset.find(target-nums[i]) != hset.end())
            {
                ans.push_back(hset[target-nums[i]]);
                ans.push_back(i);
                return ans;
            }
            else
            {
                hset[nums[i]]=i;
            }
        }
        return {};
        
    }
};
