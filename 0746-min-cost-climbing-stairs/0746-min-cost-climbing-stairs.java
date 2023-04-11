class Solution {
    public int minCostClimbingStairs(int[] cost) {
        
        int n = cost.length;
        
        
        for(int i=2; i<cost.length; i++) {
            cost[i] += Math.min(cost[i-1], cost[i-2]);
        }
        
        return Math.min(cost[n-1], cost[n-2]);
                
        
        
        // Greedy approach (does not work cuz not optimal)
//         while(i > 1) {
//             if (cost[i-1] < cost[i-2]) {
//                 sum += cost[i-1];
//                 i--;
//             }
//             else {
//                 sum += cost[i-2];
//                 i -= 2;
//             }
//         }
        
//         return sum;
    }
}