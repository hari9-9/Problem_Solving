class Solution {
public:
    void rev(vector<int>&nums,int start , int end)
    {
        int i,j,temp;
        while(start<end)
        {
            temp=nums[start];
            nums[start]=nums[end];
            nums[end]=temp;
            start++;
            end--;
            
        }
    }
    void rotate(vector<int>& nums, int k) {
        int len=nums.size();
        k%=len;
        rev(nums,0,len-1);
        rev(nums,0,k-1);
        rev(nums,k,len-1);
        
    }
};
