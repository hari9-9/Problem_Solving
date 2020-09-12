class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        if(nums.empty()) return {};
        while(i<(nums.size()-1))
        {
            if(!(nums[i]^nums[i+1]))
            {
                nums.erase( nums.begin() + i);
            }
            else
            {
                i++;   
            }
        }
        return nums.size();
    }
};

//second attempt

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        int l=0;
        int curr_ele;

        while(i<nums.size())
        {
            curr_ele=nums[i];
            i++;
            while(i<nums.size() && curr_ele==nums[i])
            {
                i++;
            }
            nums[l]=curr_ele;
            l++;
        }
        return l;
        
    }
};
