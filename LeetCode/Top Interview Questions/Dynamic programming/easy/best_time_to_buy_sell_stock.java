class Solution {
    public int maxProfit(int[] prices) {
        int minval = Integer.MAX_VALUE;
        int max_profit = 0;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<minval){
                minval = prices[i];
            }
            else if(prices[i]-minval>max_profit){
                max_profit = prices[i]-minval;
            }
        }
        return max_profit;
    }
}