class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n=nums.size();
        if(n<3)
            return false;
        int greater[n];
        int smaller[n];
        int m=0;
        smaller[0]=-1;
        int i;
        for(i=1;i<n;i++)
        {
            if(nums[i]<=nums[m])
            {
                smaller[i]=-1;
                m=i;
            }
            else
            {
                smaller[i]=m;
            }
        }
        m=n-1;
        greater[m]=-1;
        for(i=n-2;i>=0;i--)
        {
            if(nums[i]>=nums[m])
            {
                greater[i]=-1;
                m=i;
            }
            else
            {
                greater[i]=m;
            }
        }
        for(i=0;i<n;i++)
        {
            if(smaller[i]!=-1 && greater[i]!=-1)
            {
                return true;
            }
        }
        return false;
        
    }
};
