class Solution:
    def countBits(self, n: int) -> List[int]:
        
        array = [0] * (n+1)
        
        offset = 1
        
        for num in range(1, n+1):
            if offset*2 == num:
                offset = num
            
            array[num] = 1 + array[num - offset]
        
        return array