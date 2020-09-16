class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(target<nums[0])
        {
            return 0;
        }
        if(target>nums[nums.size()-1])
        {
            return nums.size();
        }
        int l = 0;
        int r=nums.size();
        int mid;
        while(l<=r)
        {
            mid=(l+r)/2;
            if(nums[mid]==target)
            {
                return mid;
            }
            if(nums[mid]>target)
            {
                r=mid-1;
            }
            else if(nums[mid]<target)
            {
                l=mid+1;
            }
        }
        return l;
    }
};
