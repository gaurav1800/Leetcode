class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
        int rows = grid.size();
        int columns = grid[0].size();
        
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < columns; j++) {
                if (i > 0 && j > 0) {
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
                }
                else if (i > 0) {
                    grid[i][j] += grid[i-1][0]; 
                }
                else if (j > 0) {
                    grid[i][j] += grid[0][j-1];
                }
            }
        }
        
        return grid[rows-1][columns-1];
        
    }
};