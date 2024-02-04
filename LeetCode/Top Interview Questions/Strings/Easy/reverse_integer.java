class Solution {
    public int reverse(int x) {
        // if(x>(Math.pow(2,31)-1) || x < (-1*Math.pow(2,31)))
        // {
        //     return 0;
        // }
        boolean flag = false;
        if(x<0) flag = true;
        x = Math.abs(x);
        int ans = 0;
        int d;
        while(x>0){
            d = x%10;
            if (ans > (Integer.MAX_VALUE - d) / 10) {
                return 0; 
            }
            ans=ans*10+d;
            x/=10;
        }
        // if(ans>(Math.pow(2,31)-1) || ans< (-1*Math.pow(2,31))){
        //     return 0;
        // }
        if(flag) ans*=-1;
        return ans;
    }
}


class Solution {
    public int reverse(int x) {
        long rev = 0;
        while(x != 0){
         rev = rev * 10 + x % 10;
         x /= 10;
        
        if(rev > Integer.MAX_VALUE  || rev < Integer.MIN_VALUE)
            return 0;
      }
      return (int) rev;
    }
}
