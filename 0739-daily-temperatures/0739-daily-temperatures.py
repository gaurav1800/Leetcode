class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        
        
        for idx, num in enumerate(temperatures):
            
            while stack and num > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = idx-i
            stack.append(idx)
                
        return result