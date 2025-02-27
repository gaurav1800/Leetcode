class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        x = edges[0]
        y = edges[1]
        
        for i in x:
            for j in y:
                if i == j:
                    return i