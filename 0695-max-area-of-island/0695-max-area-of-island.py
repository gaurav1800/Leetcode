class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        rows, columns = len(grid), len(grid[0])
        visit = set()

        def dfs(row, col):
            if (
                row < 0
                or row == rows
                or col < 0
                or col == columns
                or grid[row][col] == 0
                or (row, col) in visit
            ):
                return 0
            visit.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        area = 0
        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r, c))
        return area