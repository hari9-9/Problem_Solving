class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int val = 0;
        int curr = 0;
        int i;
        for(i=0;i<nums.length;i++)
        {
            if(nums[i]==1)
            {
                curr++;
            }
            else
            {
                if(curr>val)
                {
                    val=curr;
                }
                curr=0;
            }
        }
        if(curr>val)
        {
           return curr; 
        }
        else
        { 
            return val;
        }
    }
}
