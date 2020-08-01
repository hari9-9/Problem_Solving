class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;
        int sqrs[10];
        int i;
        int curr;
        int sum;
        for(i=0;i<10;i++)
        {
            sqrs[i]=i*i;
        }
        while(n!=1)
        {
            curr=n;
            sum=0;
            while(curr !=0)
            {
                sum+=sqrs[curr%10];
                curr=curr/10;
            }
            if(seen.find(sum) == seen.end())
            {
                seen.insert(sum);
                n=sum;
            }
            else
                return false;
        }
        
        return true;
        
    }
};
