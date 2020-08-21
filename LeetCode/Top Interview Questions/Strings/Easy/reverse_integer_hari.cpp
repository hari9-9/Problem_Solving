class Solution {
public:
    int reverse(int x) {
        bool flag=false;
        if(x>(pow(2,31)-1) || x<(-1*pow(2,31)))
           {
               return 0;
           }
        if(x<0)
        {
            flag= true;
        }
        x=abs(x);
        long long ans=0;
        int dig;
        while(x)
        {
            dig = x%10;
            ans = ans*10 +dig;
            x/=10;
        }
        if(ans>(pow(2,31)-1) || ans<(-1*pow(2,31)))
           {
               return 0;
           }
        if(flag)
        {
            ans*=-1;
        }
        return ans;
    }
};
