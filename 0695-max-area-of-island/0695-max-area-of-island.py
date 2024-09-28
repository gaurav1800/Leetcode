class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        result = 0
        
        def dfs(x, y, total):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and (x, y) not in visited:
                visited.add((x, y))
                total = 1
                for dx, dy in directions:
                    total += dfs(x+dx, y+dy, total)
                return total
            else:
                return 0
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    total = dfs(i, j, 0)
                    result = max(result, total)

        return result