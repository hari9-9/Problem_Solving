class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        long long max=0;
        unordered_set<int>hset;
        long long i=0;
        for(i=0;i<nums.size();i++)
        {
            max=nums[i]>max? nums[i]:max;
            if(nums[i]>=0)
            {
                if(hset.find(nums[i])==hset.end())
                {
                    hset.insert(nums[i]);
                }   
            }  
        }
        for(i=1;i<=max+1;i++)
        {
            if(hset.find(i)==hset.end())
                return i;
        }
        return -1;
    }
};
