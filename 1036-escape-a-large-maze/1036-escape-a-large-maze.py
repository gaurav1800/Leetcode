class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        
        if not blocked:
            return True
        
        
        def dfs(i, j, target, visited):
            if i < 0 or i >= 10**6 or j < 0 or j >= 10**6:
                return False
            if (i, j) in blocked or (i, j) in visited:
                return False
            visited.add((i, j))
            return (len(visited) > (1+199) * 199//2 or [i, j] == target or
                   dfs(i+1, j, target, visited) or 
                   dfs(i-1, j, target, visited) or
                   dfs(i, j+1, target, visited) or
                   dfs(i, j-1, target, visited))
        
        blocked = set(tuple(block) for block in blocked)
        
        return (dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set()))