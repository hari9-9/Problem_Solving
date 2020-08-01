class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map <int ,int> hset;
        int n = nums.size();
        int i;
        int res;
        for(i=0;i<n;i++)
        {
            hset[nums[i]] +=1;
        }
        for(i=0;i<n;i++)
        {
            if( hset[nums[i]]==1)
            {
                res=nums[i];
                break;
            }
        
        }
    return res;
    }
};
