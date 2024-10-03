class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        result = target[0]
        
        for x, y in zip(target, target[1:]):
            if x < y:
                result += y-x
                
        # Another solution
        # for i in range(1, len(target)):
        #     if target[i] > target[i-1]:
        #         result += target[i]-target[i-1]
        
        return result