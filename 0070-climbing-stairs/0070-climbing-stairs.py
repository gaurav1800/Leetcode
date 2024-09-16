class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        
        array = [1, 2, 3]
        
        for i in range(3, n):
            array.append(array[i-1] + array[i-2])
        
        return array[len(array)-1]
        