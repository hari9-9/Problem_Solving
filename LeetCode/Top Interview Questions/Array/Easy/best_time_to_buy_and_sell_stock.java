class Solution {
    public int maxProfit(int[] prices) {
        int b=0;
        int s=0;
        int i=0;
        int total=0;
        while(i<prices.length-1) {
            while(i+1<prices.length && prices[i]>=prices[i+1]){
                i++;
            }
            b = prices[i];
            while(i+1<prices.length && prices[i]<=prices[i+1]) {
                i++;
            }
            s= prices[i];
            total+=s-b;
        }
        return total;
    }
}
