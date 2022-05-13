class Solution {
    public int searchInsert(int[] nums, int target) {
        if(target<nums[0])
            return 0;
        int l=0;
        int r=nums.length-1;
        if(target>nums[r]){
            return r+1;
        }
        int mid=0;
        while(l<=r){
            mid=l+(r-l)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]<target){
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
        }
        return l;
    }
}
