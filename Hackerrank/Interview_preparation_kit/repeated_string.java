import java.util.*;

class Solution {
    
    public static long calc(String s , long n) {
        long full = n/s.length();
        long rem = n%s.length();
        long count = 0;
        char c[] = s.toCharArray();
        for(int i=0;i<s.length();i++) {
            if(c[i]=='a') count++;
        }
        count*=full;
        for(int i=0;i<rem;i++) {
            if(c[i]=='a') count++;
        }
        return count;
    } 
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        long n = scan.nextLong();
        long output = calc(s,n);
        System.out.println(output);
    }
}