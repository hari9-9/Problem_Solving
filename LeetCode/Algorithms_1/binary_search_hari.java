class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==1){
            if(nums[0]==target)
                return 0;
            else
                return -1;
        }
        int l,h,mid;
        l=0;
        h=nums.length-1;
        while(l<=h){
            mid=l+(h-l)/2;
            if(nums[mid]== target){
                return mid;
            }
            else if(nums[mid]<target){
                l=mid+1;
            }
            else{
                h=mid-1;
            }
        }
        return -1;
        
    }
}
