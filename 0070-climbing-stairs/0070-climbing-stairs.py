class Solution:
    def climbStairs(self, n: int) -> int:
        

        if n <= 3:
            return n

        result = [1, 2, 3]
        
        for i in range(3, n):
            result.append(result[i-2] + result[i-1])
        
        return result[len(result) - 1]
        
        
        
        
        
#         another solution

#         if n <= 3:
#             return n
    
#         first = 2
#         second = 3
        
#         for i in range(4, n+1):
#             temp = first + second
#             first = second
#             second = temp
        
#         return second
        