class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        heap = []
        distances = [[inf] * cols for _ in range(rows)]
        
        heapq.heappush(heap, (0, start[0], start[1])) # dist, row, col
        
        def is_valid(x, y):
            return 0 <= x < rows and 0<= y < cols and maze[x][y] == 0
        
        while heap:
            dist, x, y = heapq.heappop(heap)
            
            if [x, y] == destination:
                return dist
            
            for dx, dy in directions:
                nx, ny = x, y
                steps = 0
                
                while is_valid(nx+dx, ny+dy):
                    nx += dx
                    ny += dy
                    steps += 1
                
                if dist + steps < distances[nx][ny]:
                    distances[nx][ny] = dist+steps
                    heapq.heappush(heap, (distances[nx][ny], nx, ny))
        
        return -1 if distances[destination[0]][destination[1]] == inf else distances[destination[0]][destination[1]]
        
        