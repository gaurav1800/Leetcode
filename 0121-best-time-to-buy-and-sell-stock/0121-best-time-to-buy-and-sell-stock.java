class Solution {
    public int maxProfit(int[] prices) {
        
        int toBuy=prices[0], max=0;
        
        for(int i=1; i<prices.length; i++) {
            
            if (prices[i] < toBuy) {
                toBuy = prices[i];
            }
            else {
                max = prices[i]-toBuy > max ? prices[i]-toBuy : max;    
            }
        }
        
        return max;
        
    }
}