class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hset;
        int len = nums.size();
        int i;
        for(i=0;i<len;i++)
        {
            if(hset.count(nums[i])>0)
            {
                return true;
            }
            hset.insert(nums[i]);
        }
        return false;
        
    }
};
