class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        if n == 1 or n == 2 or n == 3 or n == 5:
            return True

        for num in (2, 3, 5):
            while n%num == 0:
                n //= num        
        
        return n == 1

        