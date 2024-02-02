import java.util.*;

class Solution {
    
    public static int countingValleys(int steps, String path) {
    // Write your code here
        int curr =0;
        int val = 0;
        boolean dip = false;
        for(int i=0;i<steps;i++) {
            char c = path.charAt(i);
            if(c=='U'){
                curr+=1;
                if(curr == 0 && dip == true){
                    val+=1;
                    dip = false;
                }
            }
            else {
                curr-=1;
                if(curr==-1 && dip == false) {
                    dip = true;
                }
            }
        }
        return val;
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        String s = scan.next();
        scan.close();
        System.out.println(countingValleys(n,s));
        
    }
}
