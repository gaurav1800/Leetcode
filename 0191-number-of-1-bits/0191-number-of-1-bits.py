class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        
        
#         slow implementation

        result = 0
    
        while n > 0:
            result += n % 2
            n >>= 1
        
        return result