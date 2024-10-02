from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY  
                return True
            return False
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        parent = {}  
        islands = 0  
        result = []  
        
        for r, c in positions:
            if (r, c) in parent:
                result.append(islands)
                continue
            
           
            parent[(r, c)] = (r, c)
            islands += 1
            
            # Try to union the current land with its neighboring lands
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:  
                    if union((r, c), (nr, nc)):
                        islands -= 1  
                        
            
            result.append(islands)
        
        return result
