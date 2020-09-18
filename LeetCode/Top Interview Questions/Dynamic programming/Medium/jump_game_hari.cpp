class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size()-1;
        int good=n;
        for(int i=n;i>=0;i--)
        {
            if(i+nums[i]>=good)
            {
                good=i;
            }
        }
        return good==0;
        
    }
};
