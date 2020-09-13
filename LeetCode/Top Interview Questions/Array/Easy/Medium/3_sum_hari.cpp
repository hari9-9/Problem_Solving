class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i=0;
        sort(nums.begin(),nums.end());
        int n =nums.size();
        int sum;
        vector<vector<int>>ans;
        for(i=0;i<n-2;i++)
        {
            if(i==0 || (i>0 && nums[i]!=nums[i-1]))
            {
                int l=i+1;
                int r=n-1;
                sum=0-nums[i];
                while(l<r)
                {
                    if(nums[l]+nums[r]==sum)
                    {
                        vector<int>trip;
                        trip.push_back(nums[i]);
                        trip.push_back(nums[l]);
                        trip.push_back(nums[r]);
                        ans.push_back(trip);
                        while(l<r && nums[l]==nums[l+1])
                        {
                            l++;
                        }
                        while(l<r && nums[r]==nums[r-1])
                        {
                            r--;
                        }
                        l++;
                        r--;
                    }
                    else if(nums[l]+nums[r]<sum)
                    {
                        l++;
                    }
                    else
                    {
                        r--;
                    }
                    
                }
            }
        }
        return ans;
        
    }
};
