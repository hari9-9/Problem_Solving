import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        HashMap<Integer,Integer> socks = new HashMap<Integer,Integer>();
        
        while(n>0) {
            
            int c = scan.nextInt();
            Integer frequency = socks.get(c);
            if(frequency == null) {
                socks.put(c,1);
            }
            else {
                socks.put(c,frequency+1);
            }
            n--;
        }
        scan.close();
        
        int pairs = 0;
        for(int frequency : socks.values()) {
            pairs+= (int) Math.floor(frequency/2);
        }
        
        System.out.println(pairs);
        
    }
}