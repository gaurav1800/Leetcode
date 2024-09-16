class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        if n < 3:
            return n
        
        first = 1
        second = 2
        
        
        for i in range(3, n+1):
            temp = second
            second += first
            first = temp
        
        return second
        
#         # another solution
#         array = [1, 2, 3]
        
#         for i in range(3, n):
#             array.append(array[i-1] + array[i-2])
        
#         return array[len(array)-1]
        