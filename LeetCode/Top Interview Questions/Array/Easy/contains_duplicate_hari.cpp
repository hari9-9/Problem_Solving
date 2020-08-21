class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if ( nums.empty() )
        {
            return false;
        }
        sort(nums.begin(), nums.end()); 
        for(int i=0;i<(nums.size()-1);i++)
        {
            if(nums[i]==nums[i+1])
            {
                return true;
            }
        }
        return false;
    }
};

// second attempt

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int len = nums.size();
        int i,j=0;
        for (i=0; i<len-1; i++)
        {
            j=i+1;
            if(nums[i] == nums[j])
            {
                return true;
            }
            
            }
               
        return false;
        
    }
};
