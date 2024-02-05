class Solution {
    public int strStr(String haystack, String needle) {
        int hayL = haystack.length();
        int nedL = needle.length();
        if(nedL==0){
            return 0;
        }
        int i=0;
        while(i<=hayL-nedL){
            String s = haystack.substring(i,i+nedL);
            //System.out.println(s);
            if(s.equals(needle)){
                return i;
            }
            i++;
        }
        return -1;
        
    }
}