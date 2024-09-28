class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        result = 0
        
        while x > 0 or y > 0:
            result += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        
        return result
        