class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        islands = 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and grid[x][y] == "1":
                visited.add((x, y))
                for dx, dy in directions:
                    dfs(x+dx, y+dy)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        
        return islands
            
            
        
        
        