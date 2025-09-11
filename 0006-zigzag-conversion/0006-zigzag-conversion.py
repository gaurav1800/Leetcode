class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        result = ["" for _ in range(numRows)]
        row = 0
        direction = 0 if numRows == 1 else 1
        
        for char in s:
            result[row] += char
            
            row += direction
            
            if row == 0 or row == numRows - 1:
                direction = -direction
        
        return "".join(result)