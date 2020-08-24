public:
    int climbStairs(int n) {
        int ways[n+1];
        ways[0] = 1;
        ways[1] = 1;
        for (int i=2; i<=n ; i++)
        {
            ways[i] = ways[i-1]+ways[i-2];
        }
        return ways[n];
    }
};


// second attempt

class Solution {
public:
    int climbStairs(int n) {
        int arr[n+1],i;
        arr[0]=1;
        arr[1]=1;
        for(i=2;i<=n;i++)
        {
            arr[i]=arr[i-1]+arr[i-2];
        }
        return arr[n];
        
    }
};
