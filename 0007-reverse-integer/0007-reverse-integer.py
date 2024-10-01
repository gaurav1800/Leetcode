class Solution:
    def reverse(self, x: int) -> int:
        
        neg = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        
        while x > 0 and x%10 == 0:
            x //= 10
            
        
        while x > 0:
            remainder = x%10
            x //= 10
            result = result * 10 + remainder
        
        result *= neg
        
        if result < -2**31 or 2**31 - 1 < result:
            return 0
        
        return result