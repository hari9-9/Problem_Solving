class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i : nums1){
            if(map.containsKey(i)){
                int curr=map.get(i);
                map.put(i,curr+1);
            }
            else{
                map.put(i,1);
            }
        }
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i:nums2){
            if(map.containsKey(i)){
                int curr = map.get(i);
                if(curr>0){
                    list.add(i);
                }
                map.put(i,curr-1);
            }
        }
        int[] ret = new int[list.size()]; 
        for(int i = 0; i < list.size();i++){
            ret[i] = list.get(i);
        }
        return ret;
    }
}
