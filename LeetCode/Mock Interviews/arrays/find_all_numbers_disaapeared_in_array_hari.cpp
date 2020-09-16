class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int>hset;
        int n=nums.size();
        int i;
        for(i=0;i<n;i++)
        {
            if(hset.find(nums[i])==hset.end())
            {
                hset.insert(nums[i]);
            }
        }
        vector<int>ans;
        for(i=1;i<=n;i++)
        {
            if(hset.find(i)==hset.end())
            {
                ans.push_back(i);
            }
        }
        return ans;
        
    }
};
