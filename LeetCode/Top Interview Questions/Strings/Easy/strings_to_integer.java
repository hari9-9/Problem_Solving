class Solution {
    public int myAtoi(String s) {
        s=s.trim();
        if(s.length()==0){
            return 0;
        }
        boolean pos = (s.charAt(0)=='+');
        boolean neg = (s.charAt(0)=='-');
        //System.out.println(neg);
        int i=0;
        long res=0;
        if(pos||neg){
            i++;
        }
        while(i<s.length() && Character.isDigit(s.charAt(i))){
            res=res*10+Character.getNumericValue(s.charAt(i));
            //System.out.println(res);
            if(neg && res>Integer.MAX_VALUE){
                return Integer.MIN_VALUE;
            }
            if(res>Integer.MAX_VALUE){
                return Integer.MAX_VALUE;
            }
            i++;
        }
        if(neg){
            res*=-1;
        }
        //System.out.println(res);
        if(res>Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        if(neg && res<Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        return (int) res;
        
    }
}