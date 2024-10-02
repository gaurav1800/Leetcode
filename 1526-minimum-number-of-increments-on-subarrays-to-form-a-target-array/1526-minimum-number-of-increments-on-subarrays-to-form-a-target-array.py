class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        result = target[0]
        
        for x, y in zip(target, target[1:]):
            if x < y:
                result += y-x
        
        return result