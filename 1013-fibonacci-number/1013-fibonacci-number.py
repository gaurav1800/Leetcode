class Solution:
    def fib(self, n: int) -> int:

        if n < 2:
            return n
        
        first = 0
        second = 1

        for i in range(n-1):
            temp = first + second
            first = second
            second = temp
        
        return second