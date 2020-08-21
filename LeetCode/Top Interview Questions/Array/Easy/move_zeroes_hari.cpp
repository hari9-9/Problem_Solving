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

// Second attempt

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow=0;
        int curr=0;
        int temp;
        for(curr=0;curr<nums.size();curr++)
        {
            if(nums[curr]!=0)
            {
                temp = nums[curr];
                nums[curr]=nums[slow];
                nums[slow] = temp;
                slow++;
            }
        }
        
    }
};
