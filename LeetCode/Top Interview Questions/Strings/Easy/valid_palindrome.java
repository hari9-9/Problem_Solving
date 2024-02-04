class Solution {
    public boolean isPalindrome(String s) {
        if(s.isEmpty()){
            return true;
        }
        int start=0;
        int stop=s.length()-1;
        while(start<=stop){
            char first = s.charAt(start);
            char last = s.charAt(stop);
            if(!Character.isLetterOrDigit(first)){
                start++;
            }
            else if(!Character.isLetterOrDigit(last)){
                stop--;
            }
            else{
                if(Character.toLowerCase(first)!=Character.toLowerCase(last)){
                    return false;
                }
                start++;
                stop--;
            }
        }
        return true;
    }
}