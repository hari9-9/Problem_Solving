class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int n = prices.size();
        int h=prices[0];
        int l=prices[0];
        int profit = 0;
        while(i<(n-1))
        {
            while (i<(n-1) && prices[i]>=prices[i+1])
            {
                i++;
            }
            l = prices[i];
            while (i<(n-1) && prices[i]<=prices[i+1])
            {
                i++;
            }
            h = prices[i];
            profit+=h-l;   
        }
        
        return(profit);
    }
};

## Second attempt

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int low = prices[0];
        int high = prices[0];
        int i=0;
        int profit = 0;
        while(i<n-1)
        {
            while(i<n-1 && prices[i]>=prices[i+1])
            {
                i++;
            }
            low=prices[i];
            while(i<n-1 && prices[i]<=prices[i+1])
            {
                i++;
            }
            high=prices[i];
            profit += high - low;
            
        }
        return profit;
        
    }
};
