class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int i;
        int l = nums.size();
        if(l==1)
        {
            return 0;
        }
        if(l==2)
        {
            if(nums[0]>nums[1])
            {
                return 0;
            }
            if(nums[1]>nums[0])
            {
                return 1;
            }
        }
        if(nums[0]>nums[1])
        {
            return 0;
        }
        if(nums[l-1]>nums[l-2])
        {
            return l-1;
        }
        for(i=1;i<l-1;i++)
        {
            if(nums[i]>nums[i-1] && nums[i]>nums[i+1])
                return i;
        }
        
        return -1;
        
        
    }
};
