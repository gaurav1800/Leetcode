import heapq
from typing import List

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        rows = len(maze)
        cols = len(maze[0])
        directions = {(1, 0): "d", (-1, 0): "u", (0, 1): "r", (0, -1): "l"}
        heap = []
        heapq.heappush(heap, (0, "", ball[0], ball[1]))  
        
        visited = dict()  
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
        
        while heap:
            dist, path, x, y = heapq.heappop(heap)
            
            if [x, y] == hole:
                return path  
            
            if (x, y) in visited and visited[(x, y)] <= (dist, path):
                continue
            
            visited[(x, y)] = (dist, path)
            
            for (dx, dy), direction in directions.items():
                nx, ny = x, y
                steps = 0
                
                while is_valid(nx + dx, ny + dy):
                    nx += dx
                    ny += dy
                    steps += 1
                    if [nx, ny] == hole:
                        break
                
                if (nx, ny) not in visited or (dist + steps, path + direction) < visited[(nx, ny)]:
                    heapq.heappush(heap, (dist + steps, path + direction, nx, ny))
        
        return "impossible"
