class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        queue = deque([start])
        visited.add(tuple(start))
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
        
        while queue:
            x, y = queue.popleft()
            
            if [x, y] == destination:
                return True
            
            for dx, dy in directions:
                nx, ny = x, y
                
                while is_valid(nx+dx, ny+dy):
                    nx += dx
                    ny += dy
                
                if (nx, ny) not in visited:
                    queue.append([nx, ny])
                    visited.add((nx, ny))
                    
        
        return False
        
                
                
        
        