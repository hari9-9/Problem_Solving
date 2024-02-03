class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> set = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            int curr = nums[i];
            if(set.containsKey(target-curr)){
                return new int[]{set.get(target-curr),i};
            }
            else{
                set.put(nums[i],i);
            }
        }
        return new int[]{};
    }
}
