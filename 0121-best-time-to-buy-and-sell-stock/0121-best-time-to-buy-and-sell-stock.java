class Solution {
    public int maxProfit(int[] prices) {
        
        int toBuy = prices[0], maxProfit = 0;
        
        for(int i=1; i<prices.length; i++) {
            if (toBuy>prices[i]) {
                toBuy = prices[i];
            }
            else if (prices[i] - toBuy > maxProfit) {
                maxProfit = prices[i] - toBuy;
            }
        }
        return maxProfit;
        
    }
}