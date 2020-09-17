class Solution {
public:
    bool canJump(vector<int>& nums) {
        int pos=nums.size()-1;
        for(int i=nums.size()-1; i>=0;i--)
        {
            if(nums[i]+i>=pos)
            {
                pos=i;
            }
        }
        return pos==0;
        
    }
};

// backtracking solution wont pass 2 test cases TLE

class Solution {
public:
    bool jump(vector<int>& nums, int curr)
    {
        if(curr==nums.size()-1)
        {
            return true;
        }
        bool ans=false;
        for(int i=1;i<=nums[curr];i++)
        {
            if(i+curr<=nums.size()-1)
            {
                ans=ans || jump(nums,curr+i);
            } 
            if(ans)
            {
                return true;
            }
        }
        return false;
    }
    
    bool canJump(vector<int>& nums) {
        return jump(nums,0);
        
    }
};
