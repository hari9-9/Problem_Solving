class Solution {
    public int maxProfit(int[] prices) {
        int i=0;
        int b=prices[0];
        int s=prices[0];
        int total = 0;
        while(i<prices.length-1){
            while(i<prices.length-1 && prices[i]>=prices[i+1])
                i++;
            b=prices[i];
            
            while(i<prices.length-1 && prices[i]<=prices[i+1])
                i++;
            s=prices[i];
            total+=s-b;
            
        }
        
        return total;
        
    }
}
