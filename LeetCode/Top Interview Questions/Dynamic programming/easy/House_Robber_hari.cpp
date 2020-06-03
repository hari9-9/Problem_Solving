// solution with dp array
/*class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        if (n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return nums[0];
        }
        if(n==2)
        {
            return(max(nums[0],nums[1]));
        }
        
        int dp[n];
        dp[0] = nums[0];
        dp[1] = max(nums[0],nums[1]);
        for(int i=2;i<n;i++)
        {
            dp[i]= max(nums[i]+dp[i-2],dp[i-1]);
        }
        return dp[n-1];
    }
};
*/

//Memory efficient solution
class Solution {
public:
    int rob(vector<int>& nums) {
        int n =nums.size(); 
        if (n == 0) 
            return 0; 

        int value1 = nums[0]; 
        if (n == 1) 
            return value1; 

        int value2 = max(nums[0], nums[1]); 
        if (n == 2) 
            return value2; 

        // contains maximum stolen value at the end 
        int max_val; 

        // Fill remaining positions 
        for (int i=2; i<n; i++) 
        { 
            max_val = max(nums[i]+value1, value2); 
            value1 = value2; 
            value2 = max_val; 
        } 

        return max_val; 
    } 
 
};
