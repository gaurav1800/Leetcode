class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int maxProfit = 0;
        int currentMin = prices[0];
        
        for(int i=1; i<prices.size(); i++) {
            maxProfit = max(maxProfit, prices[i] - currentMin);
            currentMin = min(currentMin, prices[i]);
        }
        
        return maxProfit;
    }
};