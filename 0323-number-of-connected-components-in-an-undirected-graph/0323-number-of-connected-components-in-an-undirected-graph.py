class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        result = 0
        
        graph = [[] for _ in range(n)]
        seen = set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node, seen):
            q = deque([node])
            seen.add(node)
            
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        q.append(v)
                        seen.add(v)
        
        for i in range(n):
            if i not in seen:
                bfs(i, seen)
                result += 1
        
        return result
            
        
                
        