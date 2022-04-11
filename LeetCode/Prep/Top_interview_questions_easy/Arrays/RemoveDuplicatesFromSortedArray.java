class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0;
        int j=0;
        int n = nums.length;
         while(j<n){
            if(nums[i]== nums[j])
                 j++;
            else{
                nums[i+1] = nums[j];
                i++;
            }
             
         }
        return i+1;
    }
}
