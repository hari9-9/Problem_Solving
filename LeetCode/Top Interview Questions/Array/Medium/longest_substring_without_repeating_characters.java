class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i=0;
        int j=0;
        int res=0;
        Set<Character> set = new HashSet<Character>();
        while(j<s.length()){
            if(!set.contains(s.charAt(j))){
                set.add(s.charAt(j));
                j++;
                res=Math.max(res,set.size());
            }
            else{
                set.remove(s.charAt(i));
                i++;
            }
        }
        return res;
    }
}