class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        num = 0
        y = x
        
        while y > 0:
            num = num*10 + y%10
            y //= 10
        
        return num == x