class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        up = 0
        down = len(matrix) - 1
        
        while (up <= down):
            mid = (up + down) // 2
            
            if (target < matrix[mid][0]):
                down = mid-1
            elif (target > matrix[mid][-1]):
                up = mid+1
            else:
                break
        
        # checking if up goes greater than down
        if (up > down):
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        row = (up+down) // 2
        
        while (left <= right):
            mid = (left+right) // 2
            
            if (target < matrix[row][mid]):
                right = mid-1
            elif (target > matrix[row][mid]):
                left = mid+1
            else:
                return True
        
        return False
        
        
        