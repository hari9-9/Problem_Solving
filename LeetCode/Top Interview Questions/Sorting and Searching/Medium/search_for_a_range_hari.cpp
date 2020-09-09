class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l=0;
        int r=nums.size()-1;
        int mid;
        while(l<=r)
        {
            mid= l+(r-l)/2;
            if(nums[mid]==target)
            {
                //cout<<"found";
                l=mid;
                r=mid;
                while(l>=0)
                {
                    if(nums[l]!=target)
                        break;
                    l--;
                }
                while(r<nums.size())
                {
                    if(nums[r]!=target)
                        break;
                    r++;
                }
                return {l+1,r-1};
            }
            else if(nums[mid]>target)
            {
                r=mid-1;
            }
            else
                l=mid+1;
        }
        return {-1,-1};
        
    }
};
