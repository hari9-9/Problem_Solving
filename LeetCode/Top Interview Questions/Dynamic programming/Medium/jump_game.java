class Solution {
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        dp[0]=true;
        for(int i=0;i<nums.length;i++){
            if(dp[i]){
                int j =nums[i];
                while(j!=0){
                    if(i+j<nums.length){
                        dp[i+j]=true;
                    }
                    j--;
                }
            }
            if(dp[nums.length-1]) return true;
        }
        
        return dp[nums.length-1];
    }
}