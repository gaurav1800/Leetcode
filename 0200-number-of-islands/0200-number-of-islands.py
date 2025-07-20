class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r, c):
            queue = deque([(r, c)])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            grid[r][c] = "0"
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x, y
                    if 0 <= nx+dx < len(grid) and 0 <= ny+dy < len(grid[0]) and grid[nx+dx][ny+dy] == "1":
                        queue.append((nx+dx, ny+dy))
                        grid[nx+dx][ny+dy] = "0"
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    result += 1
        return result