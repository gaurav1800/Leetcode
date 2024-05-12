class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int max_profit = 0;
        int current_min = prices[0];
        
        for(int i = 1; i < prices.size(); i++) {
            
            if (prices[i] - current_min > max_profit) {
                max_profit = prices[i] - current_min;
            }
            
            if (prices[i] < current_min) {
                current_min = prices[i];
            }
        }
        
        return max_profit;
        
        
        
//         little slower solution
//         int max_profit = 0;
//         int current_min = prices[0];
        
//         for(int i = 1; i < prices.size(); i++) {
//             max_profit = std::max(max_profit, prices[i] - current_min);
//             current_min = std::min(current_min, prices[i]);
//         }
        
//         return max_profit;
    }
};