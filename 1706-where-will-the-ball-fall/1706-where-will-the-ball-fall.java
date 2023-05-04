class Solution {
    public int[] findBall(int[][] grid) {
        
        int m = grid.length;
        int n = grid[0].length;
        
        int[] dp = new int[n];
        
        int[] ans = new int[n];
        
        Arrays.fill(ans,-1);
        
        for(int i=0; i<n; i++) {
            dp[i] = i;
        }
        
        for(int i=0; i<m; i++) {
            int[] newDP = new int[n];
            Arrays.fill(newDP, -1);
            for(int j=0; j<n; j++) {
                if (j+grid[i][j] < 0 || j + grid[i][j] == n) {
                    continue;
                }
                if (grid[i][j] == 1 && grid[i][j+1] == -1 || grid[i][j] == -1 && grid[i][j-1] == 1) {
                    continue;
                } 
                newDP[j+grid[i][j]] = dp[j];
            }
            dp = newDP;
        }
        
        for(int i=0; i<n; i++) {
            if (dp[i] != -1) {
                ans[dp[i]] = i;
            }
        }
        return ans;
    }
}