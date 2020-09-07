//Runtime: 996 ms
//Memory Usage: 10.2 MB

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int i,j,temp;
        int n=nums.size();
        for(i=0;i<n;i++)
        {
            for(j=0;j<n-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    
                }
                
            }
        }
        return nums[n-k];
        
    }
};
