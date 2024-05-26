class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        
        visit = set()
        
        rows = len(grid)
        columns = len(grid[0])
        
        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(columns)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and (i,j) not in visit:
                    islands += 1
                    dfs(i, j)
        
        return islands
        