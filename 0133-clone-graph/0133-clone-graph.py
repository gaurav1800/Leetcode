"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = collections.deque([node])
        hashMap = {node : Node(node.val)}

        while queue:
            i = queue.popleft()
            for j in i.neighbors:
                if j not in hashMap:
                    hashMap[j] = Node(j.val)
                    queue.append(j)
                hashMap[i].neighbors.append(hashMap[j])
        
        return hashMap[node]