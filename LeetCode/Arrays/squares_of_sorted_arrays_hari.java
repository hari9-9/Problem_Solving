class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int pp = 0;
        int np = 0;
        while(pp<n && nums[pp]<0)
        {
            pp++;
        }
        np=pp-1;
        int [] sorted_val = new int[n];
        int counter = 0;
        while(np>=0 && pp<n)
        {
            if(nums[np]*nums[np] < nums[pp]*nums[pp])
            {
                sorted_val[counter] = nums[np]*nums[np];
                np--;
            }
            else
            {
                sorted_val[counter] = nums[pp]*nums[pp];
                pp++;
            }
            counter++;
        }
        while(np>=0)
        {
            sorted_val[counter] = nums[np]*nums[np];
            np--;
            counter++;
        }
        while(pp<n)
        {
            sorted_val[counter] = nums[pp]*nums[pp];
            pp++;
            counter++;
        }
        return sorted_val;
    }
}
