class Solution {
    public int removeDuplicates(int[] nums) {
        int i,j;
        i=0;
        j=0;
        for(j=0;j<nums.length;j++)
        {
            if(nums[i]!=nums[j])
            {
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
    }
}
