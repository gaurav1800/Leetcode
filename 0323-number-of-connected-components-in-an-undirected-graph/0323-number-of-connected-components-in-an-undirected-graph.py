class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union function
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY  # Union the two components
                return True
            return False

        # Initial parent array where each node is its own parent
        parent = [i for i in range(n)]
        components = n  # Initially, each node is a separate component

        # Union the nodes connected by each edge
        for x, y in edges:
            if union(x, y):
                components -= 1  # Reduce the number of components if union is successful

        return components
    
    
    
#         result = 0
        
#         graph = [[] for _ in range(n)]
#         seen = set()
        
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         def bfs(node, seen):
#             q = deque([node])
#             seen.add(node)
            
#             while q:
#                 u = q.popleft()
#                 for v in graph[u]:
#                     if v not in seen:
#                         q.append(v)
#                         seen.add(v)
        
#         for i in range(n):
#             if i not in seen:
#                 bfs(i, seen)
#                 result += 1
        
#         return result
            
        
                
        