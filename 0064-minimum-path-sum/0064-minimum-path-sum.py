class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        
        for i in range(rows):
            for j in range(columns):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    grid[i][j] += grid[i-1][0]
                elif j > 0:
                    grid[i][j] += grid[0][j-1]
        
        return grid[rows-1][columns-1]
        