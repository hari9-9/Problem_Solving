class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int>hset;
        for(int i=0;i<nums.size();i++)
        {
            if(hset.find(nums[i])!=hset.end())
            {
                return nums[i];
            }
            hset.insert(nums[i]);
        }
        return -1;
    }
};
