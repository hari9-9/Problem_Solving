class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int i=0;
        int count = 0;
        for (i=0;i<n;i++)
        {
            if(nums[i]!=0)
            {
                swap(nums[count++],nums[i]);
                
            }
        }
    }
};
