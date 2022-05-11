class Solution {
    public void rotate(int[] nums, int k) {
        int start=0;
        int stop = nums.length-1;
        int mid = k%nums.length;
        rotate(nums, start, stop);
        rotate(nums , start, mid-1);
        rotate(nums,mid,stop);
        
    }
    
    public void rotate(int[] nums, int start, int stop){
        int temp;
        while(start<stop){
            temp = nums[start];
            nums[start]= nums[stop];
            nums[stop] = temp;
            start++;
            stop--;
            
        }
    }
    
    
    
}
