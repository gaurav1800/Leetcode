class Solution:
    def isUgly(self, n: int) -> bool:

        if n == 0 :
            return False
        if n == 1 or n == 2 or n == 3 or n == 5:
            return True

        while n%5 == 0:
            n /= 5
        
        while n%3 == 0:
            n /= 3
        
        while n%2 == 0:
            n /= 2
        
        if n == 1 or n == 2 or n == 3 or n == 5:
            return True
        
        return False
        

        