class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        if not blocked:
            return True
        
        # bfs solution
        blocked_set = set(tuple(b) for b in blocked)
        max_area = 200*200
        
        def bfs(start, end):
            queue = deque([start])
            visited = set()
            visited.add(tuple(start))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            def is_valid(x, y):
                return 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in blocked_set 
            
            while queue and len(visited) <= max_area:
                x, y = queue.popleft()
                
                if [x, y] == end:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x, y
                    
                    if is_valid(nx+dx, ny+dy):
                        nx += dx
                        ny += dy
                    
                        if (nx, ny) not in visited:
                            queue.append([nx, ny])
                            visited.add((nx, ny))
            
            return len(visited) > max_area
        
        return bfs(source, target) and bfs(target, source)
            
            
        
#         # dfs solution
#         def dfs(i, j, target, visited):
#             if i < 0 or i >= 10**6 or j < 0 or j >= 10**6:
#                 return False
#             if (i, j) in blocked or (i, j) in visited:
#                 return False
#             visited.add((i, j))
#             return (len(visited) > (1+199) * 199//2 or [i, j] == target or
#                    dfs(i+1, j, target, visited) or 
#                    dfs(i-1, j, target, visited) or
#                    dfs(i, j+1, target, visited) or
#                    dfs(i, j-1, target, visited))
#         blocked = set(tuple(b) for b in blocked)
        
#         return (dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set()))
